# 📘 Predicción de Puntaje ICFES Actual Basado en Condiciones Pasadas

## 📝 Descripción del Proyecto
El examen del ICFES (ahora Saber 11) ha sufrido múltiples cambios en su formato y escala de calificación a lo largo de los años. Este proyecto tiene como objetivo **estimar** cuál podría ser el puntaje que obtendría una persona **hoy**, considerando sus condiciones socioeconómicas en la época en que presentó el examen.

La idea es que cualquier usuario que presentó el ICFES hace años, introduzca datos aproximados sobre su entorno (recursos del hogar, estrato, educación de los padres, hábitos de estudio, etc.), y el modelo prediga un puntaje estimado en la escala actual (0-500).

---

## 🎯 Motivación
- La estructura y el enfoque del examen han cambiado, pasando de **conocimiento memorístico** a **competencias**.
- La escala de puntajes evolucionó:
  - **1966–1999**: 100–400
  - **2000–2013**: 0–400
  - **2014–presente**: 0–500 (media teórica 250)
- Las áreas evaluadas se consolidaron de nueve asignaturas a cinco grandes áreas:
  - Lectura crítica
  - Matemáticas
  - Ciencias naturales
  - Ciencias sociales y ciudadanas
  - Inglés

Queremos ofrecer una forma divertida y analítica de responder:  
> “Si volviera a presentar el examen hoy, ¿cuánto podría sacar con mis condiciones de aquella época?”

---

## 🧠 Metodología
1. **Análisis de datos reales** de exámenes recientes.
2. **Limpieza, exploración y feature engineering** para construir variables relevantes:
   - Recursos del hogar (PC, internet, libros, transporte, etc.)
   - Nivel socioeconómico y escolaridad de los padres
   - Hábitos de lectura y estudio
3. **Modelado predictivo**:
   - Algoritmo principal: **Random Forest Regressor**
   - Entrenamiento supervisado con puntaje global como variable objetivo.
4. **Evaluación**:
   - Métricas: MAE, R²
   - Análisis de importancia de variables (feature importance).
5. **Implementación en una app web** para predicciones personalizadas.

---

## 🚀 Estado del Proyecto
- [x] Análisis exploratorio de datos (EDA)
- [x] Preparación de variables predictoras
- [x] Entrenamiento y validación del modelo Random Forest
- [ ] Desarrollo de interfaz web (en evaluación: Tkinter, Flask/Django, o frontend con HTML/CSS/JS)
- [ ] Publicación como aplicación web interactiva

---

## 💻 Uso
> **Nota:** Instrucciones preliminares. El proyecto está en desarrollo.
