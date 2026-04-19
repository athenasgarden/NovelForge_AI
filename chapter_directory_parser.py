# chapter_blueprint_parser.py
# -*- coding: utf-8 -*-
import re

def parse_chapter_blueprint(blueprint_text: str):
    """
    Parses the entire chapter blueprint text and returns a list of dictionaries, each containing:
    {
      "chapter_number": int,
      "chapter_title": str,
      "chapter_role": str,       # Chapter Position/Role
      "chapter_purpose": str,    # Core Purpose
      "suspense_level": str,     # Suspense Density
      "foreshadowing": str,      # Foreshadowing Operation
      "plot_twist_level": str,   # Plot Twist Level
      "chapter_summary": str     # Chapter Summary
    }
    """

    # Split into chunks by empty lines to avoid confusion between chapters
    chunks = re.split(r'\n\s*\n', blueprint_text.strip())
    results = []

    # Match chapter number and title, supporting both Chinese and English formats
    # e.g.: Chapter 1 - Title OR 第1章 - 标题
    chapter_number_pattern = re.compile(r'^(?:第\s*(\d+)\s*章|Chapter\s*(\d+))\s*-\s*\[?(.*?)\]?$', re.IGNORECASE)

    role_pattern      = re.compile(r'^(?:本章定位|Chapter Role|Chapter Position)[:：]?\s*\[?(.*)\]?$', re.IGNORECASE)
    purpose_pattern   = re.compile(r'^(?:核心作用|Core Purpose)[:：]?\s*\[?(.*)\]?$', re.IGNORECASE)
    suspense_pattern  = re.compile(r'^(?:悬念密度|Suspense Density|Suspense Level)[:：]?\s*\[?(.*)\]?$', re.IGNORECASE)
    foreshadow_pattern = re.compile(r'^(?:伏笔操作|Foreshadowing)[:：]?\s*\[?(.*)\]?$', re.IGNORECASE)
    twist_pattern     = re.compile(r'^(?:认知颠覆|Plot Twist Level)[:：]?\s*\[?(.*)\]?$', re.IGNORECASE)
    summary_pattern   = re.compile(r'^(?:本章简述|Chapter Summary)[:：]?\s*\[?(.*)\]?$', re.IGNORECASE)

    for chunk in chunks:
        lines = chunk.strip().splitlines()
        if not lines:
            continue

        chapter_number   = None
        chapter_title    = ""
        chapter_role     = ""
        chapter_purpose  = ""
        suspense_level   = ""
        foreshadowing    = ""
        plot_twist_level = ""
        chapter_summary  = ""

        # Match first line for chapter number and title
        header_match = chapter_number_pattern.match(lines[0].strip())
        if not header_match:
            continue

        if header_match.group(1):
            chapter_number = int(header_match.group(1))
        else:
            chapter_number = int(header_match.group(2))
        chapter_title  = header_match.group(3).strip()

        # Match other fields from subsequent lines
        for line in lines[1:]:
            line_stripped = line.strip()
            if not line_stripped:
                continue

            m_role = role_pattern.match(line_stripped)
            if m_role:
                chapter_role = m_role.group(1).strip()
                continue

            m_purpose = purpose_pattern.match(line_stripped)
            if m_purpose:
                chapter_purpose = m_purpose.group(1).strip()
                continue

            m_suspense = suspense_pattern.match(line_stripped)
            if m_suspense:
                suspense_level = m_suspense.group(1).strip()
                continue

            m_foreshadow = foreshadow_pattern.match(line_stripped)
            if m_foreshadow:
                foreshadowing = m_foreshadow.group(1).strip()
                continue

            m_twist = twist_pattern.match(line_stripped)
            if m_twist:
                plot_twist_level = m_twist.group(1).strip()
                continue

            m_summary = summary_pattern.match(line_stripped)
            if m_summary:
                chapter_summary = m_summary.group(1).strip()
                continue

        results.append({
            "chapter_number": chapter_number,
            "chapter_title": chapter_title,
            "chapter_role": chapter_role,
            "chapter_purpose": chapter_purpose,
            "suspense_level": suspense_level,
            "foreshadowing": foreshadowing,
            "plot_twist_level": plot_twist_level,
            "chapter_summary": chapter_summary
        })

    # Sort by chapter_number and return
    results.sort(key=lambda x: x["chapter_number"])
    return results


def get_chapter_info_from_blueprint(blueprint_text: str, target_chapter_number: int):
    """
    Finds structured information for a specific chapter number in the provided blueprint text.
    Returns a dictionary with chapter details or a default structure if not found.
    """
    all_chapters = parse_chapter_blueprint(blueprint_text)
    for ch in all_chapters:
        if ch["chapter_number"] == target_chapter_number:
            return ch
    # Default return
    return {
        "chapter_number": target_chapter_number,
        "chapter_title": f"Chapter {target_chapter_number}",
        "chapter_role": "",
        "chapter_purpose": "",
        "suspense_level": "",
        "foreshadowing": "",
        "plot_twist_level": "",
        "chapter_summary": ""
    }
