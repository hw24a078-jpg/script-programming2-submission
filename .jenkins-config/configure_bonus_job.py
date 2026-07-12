#!/usr/bin/env python3
"""Apply the GitHub Push and Discord notifier configuration to one Jenkins job."""

import os
import sys
import xml.etree.ElementTree as ET


REPOSITORY_URL = "https://github.com/hw24a078-jpg/script-programming2-submission.git"
GITHUB_PROPERTY = "com.coravy.hudson.plugins.github.GithubProjectProperty"
GITHUB_TRIGGER = "com.cloudbees.jenkins.GitHubPushTrigger"
DISCORD_PUBLISHER = "nz.co.jammehcow.jenkinsdiscord.WebhookPublisher"


def add_github_configuration(root: ET.Element) -> None:
    properties = root.find("properties")
    for element in list(properties):
        if element.tag == GITHUB_PROPERTY:
            properties.remove(element)

    github_property = ET.SubElement(
        properties, GITHUB_PROPERTY, {"plugin": "github@1.43.0"}
    )
    ET.SubElement(github_property, "projectUrl").text = REPOSITORY_URL[:-4] + "/"
    ET.SubElement(github_property, "displayName").text = ""

    old_scm = root.find("scm")
    scm_index = list(root).index(old_scm)
    root.remove(old_scm)
    scm = ET.Element("scm", {"class": "hudson.plugins.git.GitSCM", "plugin": "git@5.7.0"})
    ET.SubElement(scm, "configVersion").text = "2"
    remotes = ET.SubElement(scm, "userRemoteConfigs")
    remote = ET.SubElement(remotes, "hudson.plugins.git.UserRemoteConfig")
    ET.SubElement(remote, "url").text = REPOSITORY_URL
    branches = ET.SubElement(scm, "branches")
    branch = ET.SubElement(branches, "hudson.plugins.git.BranchSpec")
    ET.SubElement(branch, "name").text = "*/main"
    ET.SubElement(scm, "doGenerateSubmoduleConfigurations").text = "false"
    ET.SubElement(scm, "submoduleCfg", {"class": "empty-list"})
    ET.SubElement(scm, "extensions")
    root.insert(scm_index, scm)

    triggers = root.find("triggers")
    for element in list(triggers):
        if element.tag == GITHUB_TRIGGER:
            triggers.remove(element)
    trigger = ET.SubElement(triggers, GITHUB_TRIGGER, {"plugin": "github@1.43.0"})
    ET.SubElement(trigger, "spec").text = ""


def add_discord_configuration(root: ET.Element, job_name: str, webhook_url: str) -> None:
    publishers = root.find("publishers")
    for element in list(publishers):
        if element.tag == DISCORD_PUBLISHER:
            publishers.remove(element)

    publisher = ET.SubElement(
        publishers, DISCORD_PUBLISHER, {"plugin": "discord-notifier@270.vb_d42434a_60e1"}
    )
    values = {
        "webhookURL": webhook_url,
        "sendOnStateChange": "false",
        "sendOnlyFailed": "false",
        "statusTitle": "Jenkins 課題実行結果",
        "branchName": "main",
        "thumbnailURL": "",
        "notes": "スクリプトプログラミング演習2",
        "customAvatarUrl": "",
        "customUsername": "Jenkins",
        "enableUrlLinking": "true",
        "enableArtifactList": "true",
        "enableFooterInfo": "true",
        "showChangeset": "true",
        "sendLogFile": "false",
        "sendStartNotification": "false",
        "scmWebUrl": REPOSITORY_URL[:-4],
    }
    for key, value in values.items():
        ET.SubElement(publisher, key).text = value

    container = ET.SubElement(publisher, "dynamicFieldContainer")
    fields = ET.SubElement(container, "fields")
    field = ET.SubElement(
        fields, "nz.co.jammehcow.jenkinsdiscord.DynamicFieldContainer_-DynamicField"
    )
    ET.SubElement(field, "key").text = "課題"
    ET.SubElement(field, "value").text = job_name


def main() -> None:
    if len(sys.argv) != 4:
        raise SystemExit("Usage: configure_bonus_job.py JOB_NAME INPUT_XML OUTPUT_XML")

    webhook_url = os.environ["DISCORD_WEBHOOK"]
    job_name, input_xml, output_xml = sys.argv[1:]
    tree = ET.parse(input_xml)
    root = tree.getroot()
    add_github_configuration(root)
    add_discord_configuration(root, job_name, webhook_url)
    tree.write(output_xml, encoding="utf-8", xml_declaration=True)


if __name__ == "__main__":
    main()
