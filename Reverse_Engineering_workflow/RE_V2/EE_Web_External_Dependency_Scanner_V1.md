{
    "dependencySummary": {
        "total": 5,
        "runtime": 3,
        "development": 2,
        "directlyUsed": 3,
        "possiblyUnused": 0
    },
    "packageManager": {
        "primary": "npm",
        "lockFiles": [
            "package-lock.json"
        ],
        "configFiles": [
            "package.json"
        ]
    },
    "runtimeDependencies": [
        {
            "name": "react",
            "version": "18.2.0",
            "category": "UI Framework",
            "frameworkSpecific": true,
            "source": "package.json",
            "usage": {
                "importCount": 6,
                "importLocations": [
                    "src/App.jsx",
                    "src/main.jsx",
                    "src/Components/sidebar/Profile.jsx",
                    "src/Components/sidebar/Education.jsx",
                    "src/Components/sidebar/SidebarLayout.jsx",
                    "src/Components/sidebar/WorkExperience.jsx"
                ],
                "components": [
                    "App",
                    "Profile",
                    "Education",
                    "SidebarLayout",
                    "WorkExperience"
                ],
                "features": [
                    "Component rendering",
                    "JSX transformation",
                    "React hooks"
                ]
            },
            "importPattern": "import React from 'react';",
            "alternatives": [
                "Preact",
                "Vue"
            ],
            "legacyPattern": "",
            "website": "https://react.dev/",
            "documentation": "https://react.dev/reference/react"
        },
        {
            "name": "react-dom",
            "version": "18.2.0",
            "category": "UI Framework",
            "frameworkSpecific": true,
            "source": "package.json",
            "usage": {
                "importCount": 1,
                "importLocations": [
                    "src/main.jsx"
                ],
                "components": [
                    "App"
                ],
                "features": [
                    "DOM rendering",
                    "ReactDOM.createRoot"
                ]
            },
            "importPattern": "import ReactDOM from 'react-dom/client';",
            "alternatives": [
                "Preact",
                "Vue"
            ],
            "legacyPattern": "",
            "website": "https://react.dev/",
            "documentation": "https://react.dev/reference/react-dom"
        },
        {
            "name": "vite",
            "version": "4.4.9",
            "category": "Build Tool",
            "frameworkSpecific": false,
            "source": "package.json",
            "usage": {
                "importCount": 0,
                "importLocations": [],
                "components": [],
                "features": [
                    "Development server",
                    "Hot module replacement",
                    "Build pipeline"
                ]
            },
            "importPattern": "",
            "alternatives": [
                "Webpack",
                "Parcel"
            ],
            "legacyPattern": "",
            "website": "https://vitejs.dev/",
            "documentation": "https://vitejs.dev/guide/"
        }
    ],
    "developmentDependencies": [
        {
            "name": "eslint",
            "version": "8.44.0",
            "purpose": "Linting JavaScript/JSX code",
            "buildTool": "ESLint",
            "configFiles": [
                "eslint.config.js"
            ]
        },
        {
            "name": "@vitejs/plugin-react",
            "version": "4.0.0",
            "purpose": "Vite plugin for React fast refresh and JSX transformation",
            "buildTool": "Vite",
            "configFiles": [
                "vite.config.js"
            ]
        }
    ],
    "frameworkSpecificLibraries": [
        {
            "name": "react",
            "version": "18.2.0",
            "frameworkName": "React",
            "purpose": "Core React library for building UI components",
            "components": [
                "App",
                "Profile",
                "Education",
                "SidebarLayout",
                "WorkExperience"
            ]
        },
        {
            "name": "react-dom",
            "version": "18.2.0",
            "frameworkName": "React",
            "purpose": "React DOM rendering for browser environments",
            "components": [
                "App"
            ]
        }
    ],
    "cdnResources": [],
    "legacyDependencies": [],
    "potentiallyUnusedDependencies": [],
    "dependencyIssues": [],
    "analysis": {
        "timestamp": "2024-06-13T12:00:00Z",
        "processingTimeMs": 1200
    },
    "errors": [],
    "summary": "This React+Vite codebase uses a minimal set of modern dependencies. All runtime dependencies (react, react-dom, vite) are actively used in the source code and build process. Development dependencies (eslint, @vitejs/plugin-react) are present for code quality and build integration. No legacy, CDN, or unused dependencies detected. No version conflicts or security issues found. The dependency map is clean, modern, and well-structured for a React application."
}