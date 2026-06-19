# Example 8: K-Means Clustering
# Clustering students by learning behavior, with Elbow and Silhouette evaluation

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

# Student behavior dataset (no labels - unsupervised)
data = {
    'student':          ['A','B','C','D','E','F','G','H','I','J','K','L'],
    'study_hours':      [  2,  3,  2,  5,  4,  5,  7,  8,  9,  8,  9, 10],
    'attendance':       [ 55, 60, 50, 75, 70, 72, 85, 88, 90, 92, 95, 98],
    'practice_tests':   [  1,  1,  0,  3,  2,  3,  5,  6,  6,  7,  7,  8],
    'assignment_score':  [ 45, 50, 40, 65, 60, 62, 78, 82, 85, 88, 90, 95],
}
df = pd.DataFrame(data)

print("=" * 55)
print("Student Behavior Data (No Labels)")
print("=" * 55)
print(df.to_string(index=False))

# Select features and scale
features = ['study_hours', 'attendance', 'practice_tests', 'assignment_score']
X = df[features]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("\n(Features scaled using StandardScaler before clustering)")

# --- Part 1: Elbow Method ---
print("\n" + "=" * 55)
print("Part 1: Elbow Method (K vs WCSS)")
print("=" * 55)

wcss = []
K_range = range(2, 7)
for k in K_range:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X_scaled)
    wcss.append(km.inertia_)
    print(f"  K={k}  WCSS={km.inertia_:.2f}")

print("\n  Look for the 'elbow' where WCSS drop slows down.")

# --- Part 2: Silhouette Score ---
print("\n" + "=" * 55)
print("Part 2: Silhouette Score")
print("=" * 55)

best_k, best_sil = 2, -1
for k in K_range:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = km.fit_predict(X_scaled)
    sil = silhouette_score(X_scaled, labels)
    marker = ""
    if sil > best_sil:
        best_sil = sil
        best_k = k
        marker = " <-- best"
    print(f"  K={k}  Silhouette={sil:.3f}{marker}")

print(f"\n  Best K by silhouette: {best_k}")

# --- Part 3: Final Clustering with best K ---
print("\n" + "=" * 55)
print(f"Part 3: K-Means with K={best_k}")
print("=" * 55)

km_final = KMeans(n_clusters=best_k, random_state=42, n_init=10)
df['cluster'] = km_final.fit_predict(X_scaled)

print(df[['student'] + features + ['cluster']].to_string(index=False))

# --- Part 4: Cluster Interpretation ---
print("\n" + "=" * 55)
print("Part 4: Cluster Interpretation (mean values)")
print("=" * 55)

cluster_summary = df.groupby('cluster')[features].mean().round(1)
print(cluster_summary)

print("\nInterpretation:")
for c in sorted(df['cluster'].unique()):
    row = cluster_summary.loc[c]
    avg_study = row['study_hours']
    if avg_study <= 3:
        label = "At-risk learners"
    elif avg_study <= 6:
        label = "Developing learners"
    else:
        label = "Strong learners"
    students = df[df['cluster'] == c]['student'].tolist()
    print(f"  Cluster {c}: {label} -> Students {students}")

print("\nKey Takeaway:")
print("- K-Means discovers groups without labels")
print("- Always scale features before clustering")
print("- Use Elbow + Silhouette together to pick K")
print("- Humans must interpret what clusters mean")
