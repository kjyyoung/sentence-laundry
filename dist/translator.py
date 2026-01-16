import random
import difflib
from googletrans import Translator

class SentenceLaunderer:
    def __init__(self):
        self.translator = Translator()
        # Common language codes for random selection
        self.languages = [
            'en', 'ja', 'zh-cn', 'es', 'fr', 'de', 'ru', 'ar', 'vi', 'th', 'it', 'pt'
        ]

    def wash_loop(self, text: str, chain: list = None, random_count: int = 0) -> dict:
        """
        Launders text through a chain of languages and back to original.
        
        Args:
            text (str): Input text.
            chain (list): List of language codes to pass through.
            random_count (int): If > 0, inserts this many random languages into the chain.
        """
        if not text:
            return {"error": "No text provided"}

        original_lang = 'en'
        
        current_text = text
        
        # Build the chain
        if chain is None:
            chain = ['en', 'ja'] # Default cycle
            
        if random_count > 0:
            # Random "laundering" cycles
            chain = random.sample(self.languages, random_count)

        full_chain = chain + [original_lang] # Back to KO
        
        steps = []
        previous_lang = original_lang
        
        try:
            for target_lang in full_chain:
                # Translation
                result = self.translator.translate(current_text, src=previous_lang, dest=target_lang)
                translated_text = result.text
                
                steps.append({
                    "src": previous_lang,
                    "dest": target_lang,
                    "text": translated_text
                })
                
                current_text = translated_text
                previous_lang = target_lang
                
        except Exception as e:
            return {
                "error": str(e),
                "partial_steps": steps
            }

        # Calculate "Laundry Score" (Destruction Index)
        # 1. Length difference ratio
        len_diff = abs(len(text) - len(current_text))
        
        # 2. Similarity (using difflib)
        similarity = difflib.SequenceMatcher(None, text, current_text).ratio()
        destruction_score = (1 - similarity) * 100 
        
        return {
            "original": text,
            "laundered_result": current_text,
            "chain": full_chain,
            "steps": steps,
            "metrics": {
                "length_diff": len_diff,
                "similarity": round(similarity, 4),
                "laundry_score": round(destruction_score, 2)
            }
        }

if __name__ == "__main__":
    # Test run
    machine = SentenceLaunderer()
    input_text = "오늘 점심은 진짜 맛있는 제육볶음을 먹고 싶다."
    print("--- Standard Wash ---")
    print(machine.wash_loop(input_text))
    
    print("\n--- Random Wash (2 cycles) ---")
    print(machine.wash_loop(input_text, chain=None, random_count=2))
