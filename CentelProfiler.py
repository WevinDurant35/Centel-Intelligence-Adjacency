# Centel Behavioral Profiler and Role Sorter
# Version: DSM-X v6.0 (Hardened)

import json
import random
import hashlib
import sys

CATEGORIES = {
    "Memetic Research & Deployment": [
        "Meme Nigga",
        "Anti-Propaganda Department",
        "Anti-Anti-Anti-Propaganda Department",
        "PDF Design & Typeface Ops",
        "Digital Klepto"
    ],
    "Counterfactual Department": [
        "No AI Analyst",
        "Google Page 107 Scanner",
        "Bleeding Eyeballs Overseer"
    ],
    "OSINT Lite™": [
        "Just Notices Things",
        "Digital Forensics Timestamp Guy",
        "YouTube Comment Guy"
    ],
    "Special Taskforce Units": [
        "Build-A-Bear Counter-Counter-Intel Officer",
        "Culturally Unplugged Guy",
        "Wildlife Biologist",
        "Paparazzi Division",
        "Vice Revivals Unit",
        "Guy Who Always Has Transportation"
    ],
    "Vice Revivals Unit": [
        "Misconduct Historian",
        "Repressed Memory Cartographer",
        "Guy Who Had Too Much Fun in 2009"
    ],
    "Compliance Team": [
        "Technically Might Not Be Illegal Guy"
    ],
    "Reverse Turing Test Division (RTTD)": [
        "The 1 in a Billion Reversal (Espionage Archivist)"
    ],
    "NSC Division": [
        "Plagiarist Zine Artist",
        "Passive-Aggressive Bio Forger"
    ],
    "Brain Rot Division": [
        "STEM TikTok Scroller",
        "Quantum Shrek Theorist",
        "Newton Had Rizz Believer"
    ],
    "NASA Division": [
        "Dr. Crumblestix (plush raccoon)",
        "Clipart Physicist",
        "ASCII Dream Coder"
    ]
}

BEHAVIOR_VECTORS = {
    "chaotic": ["Memetic Research & Deployment", "RTTD", "Brain Rot Division"],
    "cryptic": ["OSINT Lite™", "NSC Division"],
    "morally flexible": ["Special Taskforce Units", "Digital Klepto"],
    "deeply unserious": ["Vice Revivals Unit", "NASA Division"],
    "dangerously competent": ["Counterfactual Department", "Reverse Turing Test Division"],
    "legally decorative": ["Compliance Team"]
}

# Hash-based chaos score generator
def chaos_score(text):
    hashed = hashlib.sha256(text.encode()).hexdigest()
    score = sum([int(char, 16) for char in hashed if char.isdigit()]) % 100
    return score

def profile_and_sort(applicant_text):
    score = chaos_score(applicant_text)
    
    if score > 90:
        trait = "dangerously competent"
    elif score > 75:
        trait = "chaotic"
    elif score > 60:
        trait = "morally flexible"
    elif score > 45:
        trait = "deeply unserious"
    elif score > 30:
        trait = "cryptic"
    else:
        trait = "legally decorative"

    possible_departments = BEHAVIOR_VECTORS.get(trait, ["Compliance Team"])
    selected_dept = random.choice(possible_departments)

    # SAFETY NET: Auto-create placeholder roles if dept is missing
    if selected_dept not in CATEGORIES:
        CATEGORIES[selected_dept] = [f"Placeholder Role in {selected_dept}"]

    assigned_role = random.choice(CATEGORIES[selected_dept])

    verdict = {
        "Chaos Score": score,
        "Trait": trait,
        "Assigned Division": selected_dept,
        "Assigned Role": assigned_role
    }

    onboarding_message = f"""Welcome to Centel.
You’ve been sorted into the {selected_dept} as our new '{assigned_role}'.
We don’t pay. You don’t quit. Good luck."""

    return onboarding_message, verdict

# Execute for CLI or AppleScript shell input
if __name__ == "__main__":
    try:
        sample_text = sys.argv[1] if len(sys.argv) > 1 else input("Paste applicant input: ")
        onboarding, report = profile_and_sort(sample_text)
        print(onboarding)
        print("\nBehavioral Report:")
        print(json.dumps(report, indent=4))
    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)