"""
Simple Recommendation Engine
Industry: E-commerce & Personalization
"""

import math


# ===============================
# 1️⃣ Similarity Calculator
# ===============================

class SimilarityCalculator:
    """Calculates similarity between two users/items"""

    @staticmethod
    def cosine_similarity(vec1, vec2):
        """Cosine similarity between two vectors"""
        if not vec1 or not vec2:
            return 0

        dot = sum(a*b for a, b in zip(vec1, vec2))
        norm1 = math.sqrt(sum(a*a for a in vec1))
        norm2 = math.sqrt(sum(b*b for b in vec2))

        if norm1 == 0 or norm2 == 0:
            return 0

        return dot / (norm1 * norm2)

    @staticmethod
    def jaccard_similarity(set1, set2):
        """Jaccard similarity between two sets"""
        if not set1 and not set2:
            return 0

        intersection = len(set1 & set2)
        union = len(set1 | set2)

        return intersection / union if union != 0 else 0


# ===============================
# 2️⃣ Candidate Generator
# ===============================

class CandidateGenerator:
    """Find candidate items based on user preferences"""

    def __init__(self, user_data):
        self.user_data = user_data

    def generate(self, user):
        """Return candidate items not yet used by user"""
        if user not in self.user_data:
            return []

        user_items = set(self.user_data[user])

        all_items = set()
        for items in self.user_data.values():
            all_items.update(items)

        candidates = list(all_items - user_items)

        return candidates


# ===============================
# 3️⃣ Scorer
# ===============================

class Scorer:
    """Scores and ranks candidate items"""

    def score_items(self, candidates):
        """Simple scoring based on item frequency"""
        scores = {}

        for item in candidates:
            scores[item] = scores.get(item, 0) + 1

        return scores

    def top_n(self, scores, n=3):
        """Return top N items"""
        ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        return [item for item, score in ranked[:n]]


# ===============================
# 4️⃣ Evaluator
# ===============================

class Evaluator:
    """Evaluates recommendation quality"""

    @staticmethod
    def precision(recommended, relevant):
        if not recommended:
            return 0

        recommended_set = set(recommended)
        relevant_set = set(relevant)

        correct = len(recommended_set & relevant_set)

        return correct / len(recommended)


# ===============================
# Sample Data
# ===============================

user_preferences = {
    "Alice": ["Laptop", "Mouse", "Keyboard"],
    "Bob": ["Laptop", "Monitor", "Mouse"],
    "Charlie": ["Keyboard", "Mouse", "Headphones"]
}


# ===============================
# Recommendation Pipeline
# ===============================

def run_recommendation(user):

    print(f"\nGenerating recommendations for: {user}")

    # Candidate generation
    generator = CandidateGenerator(user_preferences)
    candidates = generator.generate(user)

    print("Candidates:", candidates)

    # Scoring
    scorer = Scorer()
    scores = scorer.score_items(candidates)

    print("Scores:", scores)

    # Top recommendations
    recommendations = scorer.top_n(scores, 3)

    print("Top Recommendations:", recommendations)

    # Evaluation (example)
    evaluator = Evaluator()

    # Assume relevant items for testing
    relevant_items = ["Monitor", "Headphones"]

    precision = evaluator.precision(recommendations, relevant_items)

    print("Precision:", precision)


# ===============================
# Run Example
# ===============================

if __name__ == "__main__":
    run_recommendation("Alice")