# WERE MARYANNE ACHIENG-672030
# Member 3: Problem Statement & System Design

## 4️⃣ Problem Statement

**What problem is being solved?**
University students struggle with healthy eating due to time constraints, limited budgets, and lack of nutritional knowledge. Food choices are influenced by individual factors (time, budget, preferences) and environmental factors (food availability on campus) (Deliens et al., 2014).

Students frequently skip meals and fail to meet recommended nutrient intakes (Bernardo et al., 2017). Even sport science undergraduates show deficiencies in protein, fiber, and micronutrients (Rupasinghe et al., 2023).

**Target user:** University students living away from home.

**Why rule-based:** Dietary guidelines are naturally rule-based, providing transparent recommendations and handling safety decisions like allergen exclusion (Kalpakoglou et al., 2025).

## 5️⃣ Proposed System Design

**Inputs:** Age, sex, weight, height, diet type, allergies, budget, activity level.

**Outputs:** Personalized meal suggestions with explanations.

**Knowledge Representation:** Uses IF-THEN production rules—transparent, modular, and aligned with dietary guidelines (Grosan & Abraham, 2011).

**Rule Examples:**
- IF diet = vegan THEN select plant-based meals ONLY
- IF allergy = lactose THEN exclude all dairy meals
- IF goal = high-protein THEN prioritize meals with >20g protein

**Architecture:** User Input → Inference Engine → Knowledge Base → Meal Output

## 6️⃣ Conclusion

A rule-based expert system can help students with meal planning by providing transparent, personalized recommendations based on dietary guidelines.

## References

Bernardo, G. L., et al. (2017). Food intake of university students. *Revista de Nutrição, 30*(6), 847–868.

Deliens, T., et al. (2014). Determinants of eating behaviour in university students. *BMC Public Health, 14*(1), 53.

Grosan, C., & Abraham, A. (2011). Rule-based expert systems. In *Intelligent Systems* (pp. 149–184). Springer.

Kalpakoglou, K., et al. (2025). An AI-based nutrition recommendation system. *Frontiers in Nutrition, 12*, 1546107.

Rupasinghe, W. A. W. S., et al. (2023). Nutritional intake of sport undergraduates. *BMC Nutrition, 9*(1), 1-9.