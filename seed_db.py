from app import create_app, db
from app.models.ingredient import Ingredient

def seed_ingredients():
    app = create_app()
    with app.app_context():
        # Create all tables if they don't exist (necessary for first-time MySQL setup)
        print("Ensuring tables exist in MySQL...")
        db.create_all()
        
        ingredients_data = [
            # User Examples
            {
                "name": "Dimer Dilinoleyl Dimer Dilinoleate",
                "function": "Skin Conditioner",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "insufficient_data",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": True
            },
            {
                "name": "Stearyl/PPG-3 Myristyl Ether Dimer Dilinoleate",
                "function": "Skin Conditioning",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "insufficient_data",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": True
            },

            # Preservatives
            {
                "name": "Parabens",
                "function": "Preservative",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Avoid", "risk_acne_prone": "Safe",
                "is_common_allergen": True,
                "regulatory_status": "safe",
                "has_sensitization": True, "has_dermal_irritation": True, "is_occlusive": False
            },
            {
                "name": "Methylparaben",
                "function": "Preservative",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Caution", "risk_acne_prone": "Safe",
                "is_common_allergen": True,
                "regulatory_status": "safe",
                "has_sensitization": True, "has_dermal_irritation": False, "is_occlusive": False
            },
             {
                "name": "Propylparaben",
                "function": "Preservative",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Caution", "risk_acne_prone": "Safe",
                 "is_common_allergen": True,
                 "regulatory_status": "safe",
                 "has_sensitization": True, "has_dermal_irritation": False, "is_occlusive": False
            },
            {
                "name": "Phenoxyethanol",
                "function": "Preservative",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Caution", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": True, "is_occlusive": False
            },
            {
                "name": "Methylisothiazolinone",
                "function": "Preservative",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Avoid", "risk_acne_prone": "Safe",
                "is_common_allergen": True,
                "regulatory_status": "restricted",
                "has_sensitization": True, "has_dermal_irritation": True, "is_occlusive": False
            },

            # Fragrances
            {
                "name": "Fragrance",
                "function": "Scent",
                "risk_oily": "Caution", "risk_dry": "Caution", "risk_sensitive": "Avoid", "risk_acne_prone": "Caution",
                "is_common_allergen": True,
                "regulatory_status": "safe",
                "has_sensitization": True, "has_dermal_irritation": True, "is_occlusive": False
            },
            {
                "name": "Parfum",
                "function": "Scent",
                "risk_oily": "Caution", "risk_dry": "Caution", "risk_sensitive": "Avoid", "risk_acne_prone": "Caution",
                "is_common_allergen": True,
                "regulatory_status": "safe",
                "has_sensitization": True, "has_dermal_irritation": True, "is_occlusive": False
            },
            {
                "name": "Limonene",
                "function": "Fragrance Component",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Caution", "risk_acne_prone": "Safe",
                "is_common_allergen": True,
                "regulatory_status": "safe",
                "has_sensitization": True, "has_dermal_irritation": True, "is_occlusive": False
            },
            {
                "name": "Linalool",
                "function": "Fragrance Component",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Caution", "risk_acne_prone": "Safe",
                "is_common_allergen": True,
                "regulatory_status": "safe",
                "has_sensitization": True, "has_dermal_irritation": False, "is_occlusive": False
            },

            # Acids / Exfoliants
            {
                "name": "Glycolic Acid",
                "function": "Exfoliant (AHA)",
                "risk_oily": "Safe", "risk_dry": "Caution", "risk_sensitive": "Caution", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": True, "is_occlusive": False
            },
            {
                "name": "Salicylic Acid",
                "function": "Exfoliant (BHA)",
                "risk_oily": "Safe", "risk_dry": "Caution", "risk_sensitive": "Caution", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": True, "is_occlusive": False
            },
            {
                "name": "Retinol",
                "function": "Anti-aging",
                "risk_oily": "Safe", "risk_dry": "Caution", "risk_sensitive": "Avoid", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": True, "is_occlusive": False
            },

            # Comedogenic Ingredients (Acne Prone Risks)
            {
                "name": "Coconut Oil",
                "function": "Emollient",
                "risk_oily": "Avoid", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Avoid",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": True
            },
             {
                "name": "Cocos Nucifera Oil",
                "function": "Emollient",
                "risk_oily": "Avoid", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Avoid",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": True
            },
            {
                "name": "Isopropyl Myristate",
                "function": "Emollient",
                "risk_oily": "Avoid", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Avoid",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                 "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": True
            },
            {
                "name": "Lanolin",
                "function": "Emollient",
                "risk_oily": "Caution", "risk_dry": "Safe", "risk_sensitive": "Caution", "risk_acne_prone": "Caution",
                "is_common_allergen": True,
                "regulatory_status": "safe",
                "has_sensitization": True, "has_dermal_irritation": False, "is_occlusive": True
            },
            
            # Alcohols
            {
                "name": "Alcohol Denat",
                "function": "Solvent/Astringent",
                "risk_oily": "Safe", "risk_dry": "Avoid", "risk_sensitive": "Avoid", "risk_acne_prone": "Caution",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": True, "is_occlusive": False
            },
            {
                "name": "Alcohol",
                "function": "Solvent",
                "risk_oily": "Safe", "risk_dry": "Avoid", "risk_sensitive": "Avoid", "risk_acne_prone": "Caution",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                 "has_sensitization": False, "has_dermal_irritation": True, "is_occlusive": False
            },

            # Sulfates
            {
                "name": "Sodium Lauryl Sulfate",
                "function": "Surfactant",
                "risk_oily": "Safe", "risk_dry": "Avoid", "risk_sensitive": "Avoid", "risk_acne_prone": "Safe",
                "is_common_allergen": True,
                "regulatory_status": "safe",
                "has_sensitization": True, "has_dermal_irritation": True, "is_occlusive": False
            },
            {
                "name": "Sodium Laureth Sulfate",
                "function": "Surfactant",
                "risk_oily": "Safe", "risk_dry": "Caution", "risk_sensitive": "Caution", "risk_acne_prone": "Safe",
                "is_common_allergen": True,
                "regulatory_status": "safe",
                "has_sensitization": True, "has_dermal_irritation": True, "is_occlusive": False
            },

            # Humectants
            {
                "name": "Hyaluronic Acid",
                "function": "Humectant",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": False
            },
            {
                "name": "Sodium Hyaluronate",
                "function": "Humectant",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": False
            },
            {
                "name": "Glycerin",
                "function": "Humectant",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": False
            },
            {
                "name": "Panthenol",
                "function": "Humectant / Skin Conditioner",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": False
            },
            {
                "name": "Urea",
                "function": "Humectant / Exfoliant",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Caution", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": True, "is_occlusive": False
            },
            {
                "name": "Propylene Glycol",
                "function": "Humectant / Solvent",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Caution", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": True, "is_occlusive": False
            },
            {
                "name": "Butylene Glycol",
                "function": "Humectant / Solvent",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": False
            },
            {
                "name": "Squalane",
                "function": "Emollient / Humectant",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": False
            },
            {
                "name": "Allantoin",
                "function": "Skin Protectant / Humectant",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": False
            },
            {
                "name": "Betaine",
                "function": "Humectant / Anti-irritant",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": False
            },

            # Emollients & Oils
            {
                "name": "Jojoba Oil",
                "function": "Emollient",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": False
            },
            {
                "name": "Argan Oil",
                "function": "Emollient / Antioxidant",
                "risk_oily": "Caution", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Caution",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": False
            },
            {
                "name": "Shea Butter",
                "function": "Emollient / Moisturizer",
                "risk_oily": "Caution", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Caution",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": True
            },
            {
                "name": "Mineral Oil",
                "function": "Emollient / Occlusive",
                "risk_oily": "Avoid", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Avoid",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": True
            },
            {
                "name": "Petrolatum",
                "function": "Occlusive / Skin Protectant",
                "risk_oily": "Avoid", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Avoid",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": True
            },
            {
                "name": "Cetyl Alcohol",
                "function": "Emollient / Emulsifier",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": False
            },
            {
                "name": "Cetearyl Alcohol",
                "function": "Emollient / Emulsifier",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": False
            },
            {
                "name": "Stearic Acid",
                "function": "Emollient / Surfactant",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Caution",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": False
            },
            {
                "name": "Dimethicone",
                "function": "Emollient / Skin Protectant",
                "risk_oily": "Caution", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Caution",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": True
            },
            {
                "name": "Cyclomethicone",
                "function": "Emollient / Solvent",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "restricted",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": False
            },
            {
                "name": "Cyclopentasiloxane",
                "function": "Silicone / Emollient",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "restricted",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": False
            },

            # Antioxidants & Vitamins
            {
                "name": "Niacinamide",
                "function": "Antioxidant / Brightening",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": False
            },
            {
                "name": "Vitamin C",
                "function": "Antioxidant / Brightening",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Caution", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": True, "is_occlusive": False
            },
            {
                "name": "Ascorbic Acid",
                "function": "Antioxidant (Vitamin C)",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Caution", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": True, "is_occlusive": False
            },
            {
                "name": "Tocopherol",
                "function": "Antioxidant (Vitamin E)",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Caution",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": False
            },
            {
                "name": "Tocopheryl Acetate",
                "function": "Antioxidant (Vitamin E)",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Caution",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": False
            },
            {
                "name": "Resveratrol",
                "function": "Antioxidant",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": False
            },
            {
                "name": "Green Tea Extract",
                "function": "Antioxidant / Anti-inflammatory",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": False
            },
            {
                "name": "Ferulic Acid",
                "function": "Antioxidant",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": False
            },
            {
                "name": "Coenzyme Q10",
                "function": "Antioxidant / Anti-aging",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": False
            },

            # Peptides & Anti-aging
            {
                "name": "Retinyl Palmitate",
                "function": "Anti-aging (Vitamin A)",
                "risk_oily": "Safe", "risk_dry": "Caution", "risk_sensitive": "Caution", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": True, "is_occlusive": False
            },
            {
                "name": "Bakuchiol",
                "function": "Anti-aging (Retinol Alternative)",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": False
            },
            {
                "name": "Collagen",
                "function": "Anti-aging / Moisturizer",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": False
            },
            {
                "name": "Peptides",
                "function": "Anti-aging / Skin Repair",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": False
            },

            # Ceramides & Barrier Repair
            {
                "name": "Ceramide NP",
                "function": "Barrier Repair / Moisturizer",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": False
            },
            {
                "name": "Ceramide AP",
                "function": "Barrier Repair / Moisturizer",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": False
            },
            {
                "name": "Ceramide EOP",
                "function": "Barrier Repair / Moisturizer",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": False
            },
            {
                "name": "Cholesterol",
                "function": "Barrier Repair / Emollient",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": False
            },

            # Sunscreen Filters
            {
                "name": "Zinc Oxide",
                "function": "Sunscreen (Physical)",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": False
            },
            {
                "name": "Titanium Dioxide",
                "function": "Sunscreen (Physical)",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": False
            },
            {
                "name": "Oxybenzone",
                "function": "Sunscreen (Chemical)",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Avoid", "risk_acne_prone": "Caution",
                "is_common_allergen": True,
                "regulatory_status": "restricted",
                "has_sensitization": True, "has_dermal_irritation": True, "is_occlusive": False
            },
            {
                "name": "Avobenzone",
                "function": "Sunscreen (Chemical)",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Caution", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": True, "is_occlusive": False
            },
            {
                "name": "Octinoxate",
                "function": "Sunscreen (Chemical)",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Caution", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "restricted",
                "has_sensitization": False, "has_dermal_irritation": True, "is_occlusive": False
            },

            # Botanicals & Extracts
            {
                "name": "Aloe Barbadensis Leaf Juice",
                "function": "Soothing / Moisturizer",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": False
            },
            {
                "name": "Chamomile Extract",
                "function": "Anti-inflammatory / Soothing",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": False
            },
            {
                "name": "Tea Tree Oil",
                "function": "Antibacterial / Anti-acne",
                "risk_oily": "Safe", "risk_dry": "Caution", "risk_sensitive": "Caution", "risk_acne_prone": "Safe",
                "is_common_allergen": True,
                "regulatory_status": "safe",
                "has_sensitization": True, "has_dermal_irritation": True, "is_occlusive": False
            },
            {
                "name": "Centella Asiatica Extract",
                "function": "Soothing / Skin Repair",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": False
            },
            {
                "name": "Rosehip Oil",
                "function": "Emollient / Antioxidant",
                "risk_oily": "Caution", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": False
            },
            {
                "name": "Witch Hazel",
                "function": "Astringent / Toner",
                "risk_oily": "Safe", "risk_dry": "Caution", "risk_sensitive": "Caution", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": True, "is_occlusive": False
            },
            {
                "name": "Turmeric Extract",
                "function": "Anti-inflammatory / Brightening",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": False
            },
            {
                "name": "Licorice Root Extract",
                "function": "Brightening / Anti-inflammatory",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": False
            },
            {
                "name": "Lavender Oil",
                "function": "Fragrance / Soothing",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Caution", "risk_acne_prone": "Safe",
                "is_common_allergen": True,
                "regulatory_status": "safe",
                "has_sensitization": True, "has_dermal_irritation": True, "is_occlusive": False
            },

            # More Acids & Exfoliants
            {
                "name": "Lactic Acid",
                "function": "Exfoliant (AHA)",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Caution", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": True, "is_occlusive": False
            },
            {
                "name": "Mandelic Acid",
                "function": "Exfoliant (AHA)",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": False
            },
            {
                "name": "Azelaic Acid",
                "function": "Anti-acne / Brightening",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": True, "is_occlusive": False
            },
            {
                "name": "Benzoyl Peroxide",
                "function": "Anti-acne",
                "risk_oily": "Safe", "risk_dry": "Caution", "risk_sensitive": "Avoid", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": True, "is_occlusive": False
            },
            {
                "name": "Kojic Acid",
                "function": "Brightening / Skin Lightening",
                "risk_oily": "Safe", "risk_dry": "Caution", "risk_sensitive": "Caution", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": True, "has_dermal_irritation": True, "is_occlusive": False
            },
            {
                "name": "Tranexamic Acid",
                "function": "Brightening / Anti-pigmentation",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": False
            },

            # Miscellaneous Common Ingredients
            {
                "name": "Benzoic Acid",
                "function": "Preservative",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Caution", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": True, "is_occlusive": False
            },
            {
                "name": "Ethylhexylglycerin",
                "function": "Preservative Booster / Skin Conditioner",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": False
            },
            {
                "name": "Sodium Benzoate",
                "function": "Preservative",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": False
            },
            {
                "name": "Potassium Sorbate",
                "function": "Preservative",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": False
            },
            {
                "name": "EDTA",
                "function": "Chelating Agent",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": False
            },
            {
                "name": "Citric Acid",
                "function": "pH Adjuster / Exfoliant",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": False
            },
            {
                "name": "Xanthan Gum",
                "function": "Thickener / Stabilizer",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": False
            },
            {
                "name": "Carbomer",
                "function": "Thickener / Emulsion Stabilizer",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": False
            },
            {
                "name": "Polysorbate 80",
                "function": "Emulsifier",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Caution",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": False
            },
            {
                "name": "Sodium PCA",
                "function": "Humectant / Moisturizer",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": False
            },
            {
                "name": "Kaolin",
                "function": "Oil Absorber / Clay",
                "risk_oily": "Safe", "risk_dry": "Caution", "risk_sensitive": "Safe", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": False
            },
            {
                "name": "Bentonite",
                "function": "Oil Absorber / Clay",
                "risk_oily": "Safe", "risk_dry": "Caution", "risk_sensitive": "Safe", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": False
            },
            {
                "name": "Sulfur",
                "function": "Anti-acne / Antimicrobial",
                "risk_oily": "Safe", "risk_dry": "Caution", "risk_sensitive": "Caution", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": True, "is_occlusive": False
            },
            {
                "name": "Hydroquinone",
                "function": "Skin Lightening",
                "risk_oily": "Caution", "risk_dry": "Caution", "risk_sensitive": "Avoid", "risk_acne_prone": "Caution",
                "is_common_allergen": False,
                "regulatory_status": "restricted",
                "has_sensitization": True, "has_dermal_irritation": True, "is_occlusive": False
            },
            {
                "name": "Arbutin",
                "function": "Brightening / Skin Lightening",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": False
            },
            {
                "name": "Formaldehyde",
                "function": "Preservative",
                "risk_oily": "Avoid", "risk_dry": "Avoid", "risk_sensitive": "Avoid", "risk_acne_prone": "Avoid",
                "is_common_allergen": True,
                "regulatory_status": "banned",
                "has_sensitization": True, "has_dermal_irritation": True, "is_occlusive": False
            },
            {
                "name": "Triclosan",
                "function": "Antibacterial",
                "risk_oily": "Caution", "risk_dry": "Caution", "risk_sensitive": "Avoid", "risk_acne_prone": "Caution",
                "is_common_allergen": False,
                "regulatory_status": "banned",
                "has_sensitization": True, "has_dermal_irritation": True, "is_occlusive": False
            },
            {
                "name": "Water",
                "function": "Solvent / Base",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": False
            },
            {
                "name": "Aqua",
                "function": "Solvent / Base",
                "risk_oily": "Safe", "risk_dry": "Safe", "risk_sensitive": "Safe", "risk_acne_prone": "Safe",
                "is_common_allergen": False,
                "regulatory_status": "safe",
                "has_sensitization": False, "has_dermal_irritation": False, "is_occlusive": False
            }
        ]

        print(f"Seeding {len(ingredients_data)} ingredients...")
        
        for data in ingredients_data:
            ingredient = Ingredient.query.filter_by(name=data['name']).first()
            if not ingredient:
                ingredient = Ingredient(name=data['name'])
                db.session.add(ingredient)
            
            # Update or Set fields
            ingredient.function = data['function']
            ingredient.risk_oily = data['risk_oily']
            ingredient.risk_dry = data['risk_dry']
            ingredient.risk_sensitive = data['risk_sensitive']
            ingredient.risk_acne_prone = data['risk_acne_prone']
            ingredient.is_common_allergen = data['is_common_allergen']
            ingredient.regulatory_status = data.get('regulatory_status', 'safe')
            ingredient.has_sensitization = data.get('has_sensitization', False)
            ingredient.has_dermal_irritation = data.get('has_dermal_irritation', False)
            ingredient.is_occlusive = data.get('is_occlusive', False)
        
        db.session.commit()
        print("Database seeded successfully!")

if __name__ == '__main__':
    seed_ingredients()
