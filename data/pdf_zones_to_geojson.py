#!/usr/bin/env python3

import argparse
import json
import math
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PDF = ROOT / "docs" / "W22543087_1743195600.pdf"
DEFAULT_OUTPUT_DIR = ROOT / "html" / "geojson"
EARTH_RADIUS_KM = 6371.0088
CIRCLE_SEGMENTS = 72

COORD_LAT_RE = re.compile(r"(?<!\d)(\d{6})N(?!\w)")
COORD_LON_RE = re.compile(r"(?<!\d)(\d{7})[EЕ](?!\w)")
RADIUS_RE = re.compile(r"Круг\s+радиусом\s+([\d,]+)\s*км")

# The published coordinate creates an isolated 75 km spike in aerodrome area
# 11100. Keep this correction explicit and record it in feature properties.
COORDINATE_CORRECTIONS = {
    (11, "11100"): {
        (26.9647222, 52.8163889): (25.9647222, 52.8163889),
    },
}

SECTIONS = [
    {
        "appendix": 1,
        "category": "prohibited",
        "category_ru": "запретные зоны",
        "filename": "prohibited_zones.geojson",
        "expected_count": 24,
        "start": "Приложение 1",
        "end": "Приложение 2",
        "entry_re": re.compile(r"^\s*(\d+)\s+(UMP)\s+(\d+)\b", re.MULTILINE),
    },
    {
        "appendix": 2,
        "category": "danger",
        "category_ru": "опасные зоны",
        "filename": "danger_zones.geojson",
        "expected_count": 47,
        "start": "Приложение 2",
        "end": "Приложение 3",
        "entry_re": re.compile(r"^\s*(\d+)\s+(UMD)\s+(\d+)\b", re.MULTILINE),
    },
    {
        "appendix": 3,
        "category": "restricted",
        "category_ru": "зоны ограничений",
        "filename": "restricted_zones.geojson",
        "expected_count": 18,
        "start": "Приложение 3",
        "end": "Приложение 4",
        "entry_re": re.compile(r"^\s*(\d+)\s+(UMR)\s+(\d+)\b", re.MULTILINE),
    },
    {
        "appendix": 4,
        "category": "aerobatic",
        "category_ru": "пилотажные зоны",
        "filename": "aerobatic_zones.geojson",
        "expected_count": 46,
        "start": "Приложение 4",
        "end": "Приложение 6",
        "entry_re": re.compile(r"^\s*(\d+\.\d+)\s+(\d{5})\b", re.MULTILINE),
        "group_marker": "Пилотажн",
    },
    {
        "appendix": 6,
        "category": "takeoff_landing",
        "category_ru": "зоны взлета и посадки",
        "filename": "takeoff_landing_zones.geojson",
        "expected_count": 32,
        "start": "Приложение 6",
        "end": "Приложение 9",
        "entry_re": re.compile(r"^\s*(\d+\.\d+)\s+(\d{5})\b", re.MULTILINE),
        "group_marker": "Зона взлета и посадки",
    },
    {
        "appendix": 11,
        "category": "aerodrome_area",
        "category_ru": "районы аэродромов",
        "filename": "aerodrome_areas.geojson",
        "expected_count": 17,
        "start": "Приложение 11",
        "end": "Приложение 12",
        "entry_re": re.compile(r"^\s*(\d+\.\d+)\s+(\d{5})\b", re.MULTILINE),
        "group_marker": "Район аэродрома",
    },
    {
        "appendix": 13,
        "category": "drone_prohibited",
        "category_ru": "запретные зоны для полетов беспилотных летательных аппаратов",
        "filename": "drone_prohibited_zones.geojson",
        "expected_count": 646,
        "start": "Приложение 13",
        "end": None,
        "entry_re": re.compile(r"^\s*(\d+)\s+(UMU)\s+(\d+)\b", re.MULTILINE),
    },
]


def pdf_to_text(pdf_path):
    result = subprocess.run(
        ["pdftotext", "-layout", str(pdf_path), "-"],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout


def dms_to_decimal(token, degree_digits):
    degrees = int(token[:degree_digits])
    minutes = int(token[degree_digits : degree_digits + 2])
    seconds = int(token[degree_digits + 2 :])
    if minutes >= 60 or seconds >= 60:
        raise ValueError(f"Invalid DMS coordinate: {token}")
    return round(degrees + minutes / 60 + seconds / 3600, 7)


def extract_coordinates(block):
    latitudes = COORD_LAT_RE.findall(block)
    longitudes = COORD_LON_RE.findall(block)
    if len(latitudes) != len(longitudes):
        raise ValueError(
            f"Coordinate count mismatch: {len(latitudes)} latitudes, "
            f"{len(longitudes)} longitudes"
        )
    return [
        [dms_to_decimal(lon, 3), dms_to_decimal(lat, 2)]
        for lat, lon in zip(latitudes, longitudes)
    ]


def destination_point(center, radius_km, bearing_degrees):
    lon1, lat1 = map(math.radians, center)
    bearing = math.radians(bearing_degrees)
    angular_distance = radius_km / EARTH_RADIUS_KM

    lat2 = math.asin(
        math.sin(lat1) * math.cos(angular_distance)
        + math.cos(lat1) * math.sin(angular_distance) * math.cos(bearing)
    )
    lon2 = lon1 + math.atan2(
        math.sin(bearing) * math.sin(angular_distance) * math.cos(lat1),
        math.cos(angular_distance) - math.sin(lat1) * math.sin(lat2),
    )
    return [round(math.degrees(lon2), 7), round(math.degrees(lat2), 7)]


def signed_area(ring):
    return sum(
        x1 * y2 - x2 * y1
        for (x1, y1), (x2, y2) in zip(ring, ring[1:])
    ) / 2


def close_and_orient_ring(coordinates):
    ring = coordinates[:]
    if ring[0] != ring[-1]:
        ring.append(ring[0])
    if signed_area(ring) < 0:
        ring.reverse()
    return ring


def circle_polygon(center, radius_km):
    ring = [
        destination_point(
            center,
            radius_km,
            360 - index * 360 / CIRCLE_SEGMENTS,
        )
        for index in range(CIRCLE_SEGMENTS)
    ]
    ring.append(ring[0])
    return ring


def normalize_line(line):
    line = re.sub(r"^\s*\d+(?:\.\d+)?\s+", "", line)
    return re.sub(r"\s+", " ", line).strip()


def find_group_name(section_text, entry_start, marker):
    if not marker:
        return None
    for line in reversed(section_text[:entry_start].splitlines()):
        normalized = normalize_line(line)
        if marker in normalized and "воздушном пространстве" not in normalized:
            return normalized
    return None


def build_properties(config, row_number, designation, block, source_shape):
    properties = {
        "designation": designation,
        "category": config["category"],
        "category_ru": config["category_ru"],
        "source_appendix": config["appendix"],
        "source_row": row_number,
        "source_shape": source_shape,
    }

    group_name = find_group_name(
        config["section_text"],
        config["entry_start"],
        config.get("group_marker"),
    )
    if group_name:
        properties["group_name"] = group_name
    if "за исключением воздушного" in block:
        properties["has_airspace_exclusion"] = True
    if "по Государственной" in block:
        properties["follows_state_border"] = True
        properties["geometry_note"] = (
            "The PDF specifies a state-border segment; GeoJSON closes the polygon "
            "directly between the listed endpoints."
        )
    return properties


def build_feature(config, match, block):
    groups = match.groups()
    row_number = groups[0]
    designation = f"{groups[1]} {groups[2]}" if len(groups) == 3 else groups[1]
    coordinates = extract_coordinates(block)
    radius_match = RADIUS_RE.search(block)
    corrections = COORDINATE_CORRECTIONS.get((config["appendix"], designation), {})
    applied_corrections = []

    for index, coordinate in enumerate(coordinates):
        corrected = corrections.get(tuple(coordinate))
        if corrected:
            applied_corrections.append(
                {
                    "source": coordinate,
                    "corrected": list(corrected),
                }
            )
            coordinates[index] = list(corrected)

    if radius_match:
        if len(coordinates) != 1:
            raise ValueError(
                f"{designation}: circle must have one center, got {len(coordinates)}"
            )
        radius_km = float(radius_match.group(1).replace(",", "."))
        properties = build_properties(config, row_number, designation, block, "circle")
        properties["radius_km"] = radius_km
        properties["center"] = coordinates[0]
        ring = circle_polygon(coordinates[0], radius_km)
    else:
        if len(coordinates) < 3:
            raise ValueError(
                f"{designation}: polygon must have at least three points, "
                f"got {len(coordinates)}"
            )
        properties = build_properties(config, row_number, designation, block, "polygon")
        ring = close_and_orient_ring(coordinates)

    if applied_corrections:
        properties["coordinate_corrections"] = applied_corrections

    feature_id = (
        f"appendix-{config['appendix']}-"
        f"{designation.lower().replace(' ', '-').replace('.', '-')}"
    )
    return {
        "type": "Feature",
        "id": feature_id,
        "properties": properties,
        "geometry": {"type": "Polygon", "coordinates": [ring]},
    }


def extract_section(text, config):
    start = text.index(config["start"])
    end = text.index(config["end"], start) if config["end"] else len(text)
    return text[start:end]


def extract_features(text, config):
    section_text = extract_section(text, config)
    matches = list(config["entry_re"].finditer(section_text))
    if len(matches) != config["expected_count"]:
        raise ValueError(
            f"Appendix {config['appendix']}: expected {config['expected_count']} "
            f"entries, found {len(matches)}"
        )
    features = []

    for index, match in enumerate(matches):
        block_end = matches[index + 1].start() if index + 1 < len(matches) else len(section_text)
        block = section_text[match.start() : block_end]
        parse_config = {
            **config,
            "section_text": section_text,
            "entry_start": match.start(),
        }
        features.append(build_feature(parse_config, match, block))
    return features


def extract_aerohub_feature(text):
    config = {
        "appendix": 12,
        "category": "aerohub_area",
        "category_ru": "районы аэроузлов",
    }
    section_text = text[text.index("Приложение 12") : text.index("Приложение 13")]
    coordinates = extract_coordinates(section_text)
    return {
        "type": "Feature",
        "id": "appendix-12-minsk-aerohub",
        "properties": {
            "designation": "Минский аэроузел",
            "category": config["category"],
            "category_ru": config["category_ru"],
            "source_appendix": config["appendix"],
            "source_shape": "polygon",
        },
        "geometry": {
            "type": "Polygon",
            "coordinates": [close_and_orient_ring(coordinates)],
        },
    }


def extract_amended_appendix_5_feature(text):
    start = text.index("заменить позицией")
    end = text.index("пункты 2 и 3", start)
    coordinates = extract_coordinates(text[start:end])
    if len(coordinates) != 5:
        raise ValueError(
            f"Appendix 5 replacement position 00002: expected 5 points, "
            f"found {len(coordinates)}"
        )
    return {
        "type": "Feature",
        "id": "appendix-5-00002",
        "properties": {
            "designation": "00002",
            "category": "amended_appendix_5_zone",
            "category_ru": "измененная позиция приложения 5",
            "source_appendix": 5,
            "source_shape": "polygon",
            "partial_appendix_extract": True,
        },
        "geometry": {
            "type": "Polygon",
            "coordinates": [close_and_orient_ring(coordinates)],
        },
    }


def collection_bbox(features):
    points = [
        point
        for feature in features
        for ring in feature["geometry"]["coordinates"]
        for point in ring
    ]
    longitudes = [point[0] for point in points]
    latitudes = [point[1] for point in points]
    return [
        round(min(longitudes), 7),
        round(min(latitudes), 7),
        round(max(longitudes), 7),
        round(max(latitudes), 7),
    ]


def make_collection(name, features, pdf_path):
    return {
        "type": "FeatureCollection",
        "name": name,
        "source": "Постановление Министерства обороны Республики Беларусь 20.01.2025 № 1",
        "source_pdf": pdf_path.name,
        "circle_approximation_segments": CIRCLE_SEGMENTS,
        "bbox": collection_bbox(features),
        "features": features,
    }


def write_collection(path, collection):
    path.write_text(
        json.dumps(collection, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def write_browser_bundle(path, collections):
    path.write_text(
        "var zones2020Data = "
        + json.dumps(collections, ensure_ascii=False, separators=(",", ":"))
        + ";\n",
        encoding="utf-8",
    )


def convert(pdf_path, output_dir):
    text = pdf_to_text(pdf_path)
    output_dir.mkdir(parents=True, exist_ok=True)
    all_features = []
    browser_collections = {}

    amended_appendix_5_feature = extract_amended_appendix_5_feature(text)
    amended_appendix_5_collection = make_collection(
        "измененная позиция приложения 5",
        [amended_appendix_5_feature],
        pdf_path,
    )
    write_collection(
        output_dir / "amended_appendix_5_zones.geojson",
        amended_appendix_5_collection,
    )
    browser_collections["amended_appendix_5_zone"] = amended_appendix_5_collection
    all_features.append(amended_appendix_5_feature)

    for config in SECTIONS:
        features = extract_features(text, config)
        collection = make_collection(config["category_ru"], features, pdf_path)
        write_collection(output_dir / config["filename"], collection)
        browser_collections[config["category"]] = collection
        all_features.extend(features)

    aerohub_feature = extract_aerohub_feature(text)
    aerohub_collection = make_collection(
        "районы аэроузлов",
        [aerohub_feature],
        pdf_path,
    )
    write_collection(output_dir / "aerohub_areas.geojson", aerohub_collection)
    browser_collections["aerohub_area"] = aerohub_collection
    all_features.append(aerohub_feature)

    combined = make_collection("все зоны и районы", all_features, pdf_path)
    write_collection(output_dir / "all_zones.geojson", combined)
    write_browser_bundle(output_dir / "zones2020-data.js", browser_collections)


def main():
    parser = argparse.ArgumentParser(
        description="Convert zone tables from W22543087_1743195600.pdf to GeoJSON."
    )
    parser.add_argument("pdf", nargs="?", type=Path, default=DEFAULT_PDF)
    parser.add_argument("output_dir", nargs="?", type=Path, default=DEFAULT_OUTPUT_DIR)
    args = parser.parse_args()
    convert(args.pdf.resolve(), args.output_dir.resolve())


if __name__ == "__main__":
    main()
