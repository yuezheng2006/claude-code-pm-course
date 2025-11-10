#!/usr/bin/env python3
"""
Generate realistic CSV data for Module 2.2: Data-Driven Feature Development
K歌应用场景 - SingTech 移动K歌APP数据分析
Uses only Python standard library (no pandas/numpy required)
"""

import csv
import random
from datetime import datetime, timedelta
from collections import defaultdict
import math

# Set seed for reproducibility
random.seed(42)

def weighted_choice(choices, weights):
    """Select from choices with given weights"""
    total = sum(weights)
    r = random.uniform(0, total)
    upto = 0
    for choice, weight in zip(choices, weights):
        if upto + weight >= r:
            return choice
        upto += weight
    return choices[-1]

def gamma_sample(shape, scale):
    """Simple gamma distribution approximation"""
    # Using sum of exponentials approximation
    total = 0
    for _ in range(int(shape)):
        total += random.expovariate(1.0 / scale)
    return total

def normal_sample(mean, std):
    """Normal distribution using Box-Muller transform"""
    u1 = random.random()
    u2 = random.random()
    z0 = math.sqrt(-2.0 * math.log(u1)) * math.cos(2.0 * math.pi * u2)
    return mean + z0 * std

print("Generating Module 2.2 data files (K歌应用场景)...")

# ============================================================================
# FILE 1: singtech-usage-data-q4.csv (K歌APP使用数据)
# ============================================================================
print("\n1. Generating singtech-usage-data-q4.csv...")

# 用户类型:个人用户、家庭用户、年轻用户
user_types = ['年轻用户', '家庭用户', '音乐爱好者']
user_type_weights = [0.6, 0.3, 0.1]

# 年龄段
age_groups = ['18-24岁', '25-34岁', '35-44岁', '45岁以上']
# 使用场景
usage_scenarios = ['独唱', '合唱', '家庭聚会', '朋友聚会', '练歌']

start_date = datetime(2024, 10, 1)
end_date = datetime(2024, 12, 31)

users_data = []
num_users = 250

for i in range(num_users):
    user_id = f"user_{i+1:04d}"
    user_type = weighted_choice(user_types, user_type_weights)
    age_group = random.choice(age_groups)
    scenario = random.choice(usage_scenarios)

    signup_time = start_date + timedelta(
        seconds=random.randint(0, int((end_date - start_date).total_seconds()))
    )

    users_data.append({
        'user_id': user_id,
        'event_type': 'signup',
        'timestamp': signup_time.isoformat(),
        'user_type': user_type,
        'age_group': age_group,
        'usage_scenario': scenario
    })

    # 72%的用户会完成首次歌曲选择
    if random.random() < 0.72:
        song_selected_time = signup_time + timedelta(minutes=random.randint(1, 15))
        users_data.append({
            'user_id': user_id,
            'event_type': 'first_song_selected',
            'timestamp': song_selected_time.isoformat(),
            'user_type': user_type,
            'age_group': age_group,
            'usage_scenario': scenario
        })

        # 40%完成首次演唱
        completion_prob = 0.38 if user_type == '年轻用户' else 0.42
        if random.random() < completion_prob:
            song_completed_time = song_selected_time + timedelta(minutes=random.randint(3, 8))
            users_data.append({
                'user_id': user_id,
                'event_type': 'first_song_completed',
                'timestamp': song_completed_time.isoformat(),
                'user_type': user_type,
                'age_group': age_group,
                'usage_scenario': scenario
            })

            # 50%会分享作品
            if random.random() < 0.5:
                share_time = song_completed_time + timedelta(minutes=random.randint(1, 30))
                users_data.append({
                    'user_id': user_id,
                    'event_type': 'shared_recording',
                    'timestamp': share_time.isoformat(),
                    'user_type': user_type,
                    'age_group': age_group,
                    'usage_scenario': scenario
                })

with open('singtech-usage-data-q4.csv', 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.DictWriter(f, fieldnames=['user_id', 'event_type', 'timestamp', 'user_type', 'age_group', 'usage_scenario'])
    writer.writeheader()
    writer.writerows(users_data)

print(f"   ✓ Created {len(users_data)} rows")

# ============================================================================
# FILE 2: activation-funnel-q4.csv (K歌激活漏斗)
# ============================================================================
print("\n2. Generating activation-funnel-q4.csv...")

funnel_data = [
    ['注册', 10000, 10000, 1.0, 0],
    ['首次选歌', 10000, 7200, 0.72, 5],
    ['完成首次演唱', 7200, 2880, 0.40, 8],
    ['分享作品', 2880, 1440, 0.50, 3]
]

with open('activation-funnel-q4.csv', 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(['step', 'users_entered', 'users_completed', 'completion_rate', 'median_time_to_complete'])
    writer.writerows(funnel_data)

print(f"   ✓ Created {len(funnel_data)} rows")

# ============================================================================
# FILE 3: user-survey-responses.csv (用户调查反馈)
# ============================================================================
print("\n3. Generating user-survey-responses.csv...")

confusion_themes = {
    "不知道唱什么歌": [
        "不知道该选什么歌唱",
        "歌库太大,不知道从哪里开始",
        "盯着歌单不知道选什么",
        "找不到适合自己的歌",
        "不确定哪首歌适合我的音域"
    ],
    "需要推荐": [
        "需要一些歌曲推荐",
        "希望有新手推荐歌单",
        "想看看别人都在唱什么",
        "需要适合我音域的歌曲推荐",
        "希望APP能根据我的嗓音推荐歌"
    ],
    "空白界面压力": [
        "空白的界面让我不知所措",
        "没有引导,不知道从哪里开始",
        "作为新手感觉很迷茫",
        "太多功能,不知道先用哪个",
        "界面功能太多,找不到入口"
    ],
    "其他": [
        "导航不够清晰",
        "找不到我想要的功能",
        "操作太复杂",
        "界面不够直观",
        "和我预期的不一样"
    ]
}

feature_requests = {
    "不知道唱什么歌": "新手推荐歌单",
    "需要推荐": "智能歌曲推荐",
    "空白界面压力": "新手引导教程",
    "其他": "更好的帮助文档"
}

survey_data = []
for i in range(800):
    user_id = f"survey_user_{i+1:04d}"
    user_type = weighted_choice(user_types, user_type_weights)

    if user_type == '年轻用户':
        theme_weights = [0.42, 0.33, 0.20, 0.05]
    else:
        theme_weights = [0.25, 0.20, 0.25, 0.30]

    theme = weighted_choice(list(confusion_themes.keys()), theme_weights)
    confusion_text = random.choice(confusion_themes[theme])

    survey_data.append({
        'user_id': user_id,
        'user_type': user_type,
        'onboarding_rating': random.randint(2, 4),
        'biggest_confusion': confusion_text,
        'feature_request': feature_requests[theme],
        'would_recommend': random.choice(['No', 'Maybe', 'Maybe', 'Yes'])
    })

with open('user-survey-responses.csv', 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.DictWriter(f, fieldnames=['user_id', 'user_type', 'onboarding_rating', 'biggest_confusion', 'feature_request', 'would_recommend'])
    writer.writeheader()
    writer.writerows(survey_data)

print(f"   ✓ Created {len(survey_data)} rows")

# ============================================================================
# FILE 4: onboarding-experiment-results.csv (新手引导实验数据)
# ============================================================================
print("\n4. Generating onboarding-experiment-results.csv...")

experiment_data = []

user_type_dist = {
    '年轻用户': 2400,
    '家庭用户': 1200,
    '音乐爱好者': 400
}

user_counter = 0

for cohort in ['control', 'treatment']:
    for user_type, count in user_type_dist.items():
        if cohort == 'control':
            if user_type == '年轻用户':
                activation_rate = 0.448
            elif user_type == '家庭用户':
                activation_rate = 0.455
            else:
                activation_rate = 0.456
        else:  # treatment - 新手推荐歌单
            if user_type == '年轻用户':
                activation_rate = 0.562  # 年轻用户提升明显
            elif user_type == '家庭用户':
                activation_rate = 0.471  # 家庭用户提升一般
            else:
                activation_rate = 0.421  # 音乐爱好者反而下降(他们有自己的选歌偏好)

        for i in range(count):
            user_id = f"{cohort}_user_{user_counter:04d}"
            user_counter += 1
            age_group = random.choice(age_groups)

            signup_date = datetime(2024, 10, 1) + timedelta(days=random.randint(0, 60))
            completed_first_song = random.random() < activation_rate

            if completed_first_song:
                if cohort == 'treatment':
                    time_to_first_song = int(gamma_sample(2, 3))  # 更快完成
                else:
                    time_to_first_song = int(gamma_sample(3, 5))
            else:
                time_to_first_song = None

            # Treatment组有更高的分享率和歌单使用率
            shared_recording = random.random() < (0.348 if cohort == 'treatment' else 0.121)
            used_recommended_playlist = random.random() < (0.352 if cohort == 'treatment' else 0.109)

            if completed_first_song:
                if cohort == 'treatment':
                    days_active = min(7, max(0, int(normal_sample(5.5, 1.5))))
                    songs_completed = max(1, int(gamma_sample(3, 2.3)))
                else:
                    days_active = min(7, max(0, int(normal_sample(4.2, 2))))
                    songs_completed = max(1, int(gamma_sample(2, 1.5)))
            else:
                days_active = min(7, max(0, int(random.expovariate(1.0))))
                songs_completed = 0

            experiment_data.append({
                'user_id': user_id,
                'cohort': cohort,
                'signup_date': signup_date.strftime('%Y-%m-%d'),
                'user_type': user_type,
                'age_group': age_group,
                'completed_first_song': str(completed_first_song),
                'time_to_first_song_minutes': time_to_first_song if time_to_first_song is not None else '',
                'shared_recording': str(shared_recording),
                'used_recommended_playlist': str(used_recommended_playlist),
                'days_active_week_1': days_active,
                'songs_completed_week_1': songs_completed
            })

with open('onboarding-experiment-results.csv', 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.DictWriter(f, fieldnames=['user_id', 'cohort', 'signup_date', 'user_type', 'age_group',
                                            'completed_first_song', 'time_to_first_song_minutes', 'shared_recording',
                                            'used_recommended_playlist', 'days_active_week_1', 'songs_completed_week_1'])
    writer.writeheader()
    writer.writerows(experiment_data)

print(f"   ✓ Created {len(experiment_data)} rows")

# ============================================================================
# VALIDATION: Print statistics to verify
# ============================================================================
print("\n" + "="*70)
print("VALIDATION: Checking experiment statistics")
print("="*70)

# Calculate statistics
control_data = [r for r in experiment_data if r['cohort'] == 'control']
treatment_data = [r for r in experiment_data if r['cohort'] == 'treatment']

control_activated = [r for r in control_data if r['completed_first_song'] == 'True']
treatment_activated = [r for r in treatment_data if r['completed_first_song'] == 'True']

control_rate = len(control_activated) / len(control_data)
treatment_rate = len(treatment_activated) / len(treatment_data)

print(f"\n📊 Overall Activation Rates (完成首次演唱):")
print(f"   Control:   {control_rate:.3f} (target: 0.452)")
print(f"   Treatment: {treatment_rate:.3f} (target: 0.478)")
print(f"   Lift:      {(treatment_rate - control_rate):.3f} (target: 0.026)")

print(f"\n📊 Activation Rates by Segment (按用户类型):")
for user_type in ['年轻用户', '家庭用户', '音乐爱好者']:
    control_seg = [r for r in control_data if r['user_type'] == user_type]
    treatment_seg = [r for r in treatment_data if r['user_type'] == user_type]

    control_seg_activated = len([r for r in control_seg if r['completed_first_song'] == 'True'])
    treatment_seg_activated = len([r for r in treatment_seg if r['completed_first_song'] == 'True'])

    control_seg_rate = control_seg_activated / len(control_seg)
    treatment_seg_rate = treatment_seg_activated / len(treatment_seg)
    lift = treatment_seg_rate - control_seg_rate

    print(f"\n   {user_type:12s}")
    print(f"      Control:   {control_seg_rate:.3f}")
    print(f"      Treatment: {treatment_seg_rate:.3f}")
    print(f"      Lift:      {lift:+.3f}")

# Retention
control_retention = len([r for r in control_activated if int(r['days_active_week_1']) >= 3]) / len(control_activated)
treatment_retention = len([r for r in treatment_activated if int(r['days_active_week_1']) >= 3]) / len(treatment_activated)

print(f"\n📊 Week 1 Retention (Activated Users Only):")
print(f"   Control:   {control_retention:.3f} (target: ~0.601)")
print(f"   Treatment: {treatment_retention:.3f} (target: ~0.784)")
print(f"   Lift:      {(treatment_retention - control_retention):+.3f}")

# Songs completed
control_songs = sum(int(r['songs_completed_week_1']) for r in control_activated) / len(control_activated)
treatment_songs = sum(int(r['songs_completed_week_1']) for r in treatment_activated) / len(treatment_activated)

print(f"\n📊 Songs Completed (Week 1, Activated Users):")
print(f"   Control:   {control_songs:.1f} songs (target: ~2.9)")
print(f"   Treatment: {treatment_songs:.1f} songs (target: ~6.8)")
print(f"   Ratio:     {treatment_songs/control_songs:.1f}x")

# Feature adoption
control_playlists = len([r for r in control_data if r['used_recommended_playlist'] == 'True']) / len(control_data)
treatment_playlists = len([r for r in treatment_data if r['used_recommended_playlist'] == 'True']) / len(treatment_data)

control_shares = len([r for r in control_data if r['shared_recording'] == 'True']) / len(control_data)
treatment_shares = len([r for r in treatment_data if r['shared_recording'] == 'True']) / len(treatment_data)

print(f"\n📊 Feature Adoption:")
print(f"   Recommended Playlist Usage:")
print(f"      Control:   {control_playlists:.3f} (target: ~0.109)")
print(f"      Treatment: {treatment_playlists:.3f} (target: ~0.352)")
print(f"      Ratio:     {treatment_playlists/control_playlists:.1f}x")
print(f"\n   Share Recording:")
print(f"      Control:   {control_shares:.3f} (target: ~0.121)")
print(f"      Treatment: {treatment_shares:.3f} (target: ~0.348)")
print(f"      Ratio:     {treatment_shares/control_shares:.1f}x")

print("\n" + "="*70)
print("✅ All files generated successfully!")
print("="*70)
print("\nGenerated files:")
print("   1. singtech-usage-data-q4.csv")
print("   2. activation-funnel-q4.csv")
print("   3. user-survey-responses.csv")
print("   4. onboarding-experiment-results.csv")
print("\nReady for Module 2.2 (K歌应用场景)! 🎉")
