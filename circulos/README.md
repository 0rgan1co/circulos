# Círculos Impacto+ | Pitch Deck

> Presentación de slides interactiva construida con [Slidev](https://sli.dev/) para el programa de antifragilidad para startups de base científica y tecnológica en el Sur Global.

## 📋 Descripción

**Círculos Impacto+** es una comunidad de aprendizaje entre pares enfocada en evolucionar el modelo de startups con impacto+ en el Sur Global. Este repositorio contiene la presentación del pitch deck utilizada para comunicar la propuesta de valor, el modelo de negocio y la teoría de cambio del programa.

La presentación está desarrollada con **Slidev**, un framework moderno para crear presentaciones desde Markdown con soporte para:
- ✅ Componentes Vue interactivos
- ✅ Temas personalizados
- ✅ Sintaxis Markdown extendida
- ✅ Exportación a PDF/PNG
- ✅ Presentador mode con notas

## 🚀 Inicio Rápido

### Prerequisitos

- Node.js 20+ instalado
- npm o pnpm

### Instalación

```bash
# Clonar el repositorio
git clone https://github.com/0rgan1co/circulos.git

# Navegar al directorio
cd circulos/circulos

# Instalar dependencias
pnpm install
```

### Desarrollo

```bash
# Iniciar servidor de desarrollo
pnpm dev

# El servidor estará disponible en:
# http://localhost:3030
```

Visita `http://localhost:3030` en tu navegador para ver la presentación en modo desarrollo.

### Build para Producción

```bash
# Construir versión estática
pnpm build

# Los archivos se generarán en /dist
```

### Exportar

```bash
# Exportar a PDF (requiere playwright instalado)
pnpm export
```

## 📂 Estructura del Proyecto

```
circulos/
├── components/        # Componentes Vue reutilizables
├── pages/            # Páginas adicionales de Slidev
├── public/           # Assets estáticos (imágenes, etc.)
├── snippets/         # Fragmentos de código reutilizables
├── slides.md         # ⭐ Contenido principal de la presentación
├── package.json      # Dependencias y scripts
├── netlify.toml      # Configuración de despliegue en Netlify
├── vercel.json       # Configuración de despliegue en Vercel
└── mcp_ui.py         # Script auxiliar para consulta de Neo4j
```

## 📊 Contenido de la Presentación

La presentación cubre los siguientes temas (21 slides):

1. **Introducción** - ¿Qué es la antifragilidad?
2. **Índice** - Estructura de la presentación
3. **El Problema** - Fragilidad y soledad del founder
4. **Estadísticas** - Datos sobre mortalidad de startups
5. **Público Objetivo** - Para quién es (y no es) el programa
6. **Tamaño del Mercado** - TAM/SAM/SOM análisis
7. **La Solución** - Qué es Círculos Impacto+
8. **Movimientos Clave** - Transformaciones que impulsamos
9. **Teoría del Cambio** - Marco Doughnut Economics
10. **¿Por qué ahora?** - Ventana 2026-2027
11. **Posicionamiento** - Comparación con YPO/Endeavor/Vistage
12. **Propuesta Económica** - Pricing y valor para founders
13. **Ingresos** - Modelo de negocio y métricas clave
14. **Egresos Piloto** - Desglose de costos
15. **Riesgos** - Principales riesgos y mitigaciones
16. **Roadmap 2026** - Q1 Validación → Q2 Expansión → Q3-Q4 Escala
17. **Apéndice** - Información complementaria
18. **Framework Antifragilidad Score™** - 5 dimensiones
19. **Crecimiento 5 Años** - Proyecciones conservadoras
20. **Call to Action** - Próximos pasos
21. **Cierre** - ¡Gracias!

## 🎨 Personalización

### Editar Contenido

El contenido principal se encuentra en `slides.md`. Este archivo usa sintaxis Markdown extendida con frontmatter YAML para configuración:

```markdown
---
theme: default
background: https://images.unsplash.com/...
highlighter: shiki
lineNumbers: false
title: Círculos Impacto+ - Pitch Deck
---

# Tu Slide

Contenido...
```

### Themes y Estilos

El proyecto usa:
- **Theme**: `default` de Slidev con temas personalizados (`theme-default`, `theme-seriph`)
- **Syntax highlighting**: Shiki
- **Framework**: Vue 3.5.26

## 🛠 Tecnologías Utilizadas

- **[Slidev](https://sli.dev/)** (v0.52.11) - Framework de presentaciones
- **[Vue.js](https://vuejs.org/)** (v3.5.26) - Framework reactivo
- **Node.js** (v20) - Runtime de JavaScript
- **Netlify/Vercel** - Plataformas de hosting
- **Python/Streamlit** - Script auxiliar para integración con Neo4j

## 🔗 Scripts Auxiliares

### `mcp_ui.py` - Interfaz de Consulta Neo4j

Script de Streamlit para consultar una base de datos Neo4j mediante lenguaje natural:

```bash
# Instalar dependencias
pip install streamlit requests

# Ejecutar la interfaz
streamlit run mcp_ui.py
```

Requiere:
- URL de MCP (Model Context Protocol) en Cloud Run
- Opcional: API Key de Gemini para convertir lenguaje natural a Cypher

## 🌐 Despliegue

### Netlify

El proyecto está configurado para despliegue automático en Netlify:
- **Build command**: `npm run build`
- **Publish directory**: `dist`
- **Node version**: 20

### Vercel

También compatible con Vercel mediante `vercel.json`.

## 📚 Recursos

- [Documentación de Slidev](https://sli.dev/)
- [Guía de Markdown de Slidev](https://sli.dev/guide/syntax)
- [Doughnut Economics](https://doughnuteconomics.org/)
- [Framework Antifragilidad - Nassim Taleb](https://www.fooledbyrandomness.com/)

## 📄 Licencia

Este proyecto es propiedad de 0rgan1co.

## 👥 Contribuciones

Este es un repositorio privado de pitch deck. Para más información sobre el programa Círculos Impacto+, contactar a través del repositorio.

## 📞 Contacto

Para más información o para unirte al programa:
- 📱 WhatsApp: [Escanea el QR en la slide 20]
- 🌐 GitHub: [@0rgan1co](https://github.com/0rgan1co)

---

**Versión actual**: v5.0  
**Última actualización**: Enero 2026
