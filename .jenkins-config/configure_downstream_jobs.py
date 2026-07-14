#!/usr/bin/env python3
"""Add downstream Jenkins jobs to an existing freestyle-job XML file."""

import sys
import xml.etree.ElementTree as ET


BUILD_TRIGGER = "hudson.tasks.BuildTrigger"


def main() -> None:
    if len(sys.argv) < 4:
        raise SystemExit(
            "Usage: configure_downstream_jobs.py INPUT_XML OUTPUT_XML JOB [JOB ...]"
        )

    input_xml, output_xml, *jobs = sys.argv[1:]
    tree = ET.parse(input_xml)
    root = tree.getroot()
    publishers = root.find("publishers")

    for publisher in list(publishers):
        if publisher.tag == BUILD_TRIGGER:
            publishers.remove(publisher)

    trigger = ET.Element(BUILD_TRIGGER)
    ET.SubElement(trigger, "childProjects").text = ", ".join(jobs)
    ET.SubElement(trigger, "threshold").text = "SUCCESS"
    publishers.insert(0, trigger)

    tree.write(output_xml, encoding="utf-8", xml_declaration=True)


if __name__ == "__main__":
    main()
