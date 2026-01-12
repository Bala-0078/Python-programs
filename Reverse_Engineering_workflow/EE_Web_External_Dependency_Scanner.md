{
  "dependencySummary": {
    "total": 6,
    "runtime": 6,
    "development": 9,
    "directlyUsed": 6,
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
      "version": "19.2.3",
      "category": "core framework",
      "frameworkSpecific": true,
      "source": "package.json",
      "usage": {
        "importCount": 2,
        "importLocations": [
          "src/main.jsx",
          "src/App.jsx"
        ],
        "components": [
          "App",
          "ReactDOM.createRoot"
        ],
        "features": [
          "Component rendering",
          "JSX transformation"
        ]
      },
      "importPattern": "import React from 'react'",
      "alternatives": [
        "preact"
      ],
      "legacyPattern": "",
      "website": "https://react.dev/",
      "documentation": "https://react.dev/reference/react"
    },
    {
      "name": "react-dom",
      "version": "19.2.3",
      "category": "core framework",
      "frameworkSpecific": true,
      "source": "package.json",
      "usage": {
        "importCount": 1,
        "importLocations": [
          "src/main.jsx"
        ],
        "components": [
          "ReactDOM.createRoot"
        ],
        "features": [
          "DOM rendering"
        ]
      },
      "importPattern": "import ReactDOM from 'react-dom/client'",
      "alternatives": [
        "preact"
      ],
      "legacyPattern": "",
      "website": "https://react.dev/",
      "documentation": "https://react.dev/reference/react-dom"
    },
    {
      "name": "@mui/material",
      "version": "7.3.6",
      "category": "UI Components",
      "frameworkSpecific": true,
      "source": "package.json",
      "usage": {
        "importCount": 3,
        "importLocations": [
          "src/App.jsx",
          "src/Components/sidebar/Profile.jsx",
          "src/Components/sidebar/SidebarLayout.jsx"
        ],
        "components": [
          "Button",
          "Typography",
          "Box",
          "Stack",
          "Paper",
          "Avatar"
        ],
        "features": [
          "Material Design UI components"
        ]
      },
      "importPattern": "import { Button } from '@mui/material'",
      "alternatives": [
        "Ant Design",
        "Chakra UI"
      ],
      "legacyPattern": "",
      "website": "https://mui.com/",
      "documentation": "https://mui.com/material-ui/"
    },
    {
      "name": "@mui/icons-material",
      "version": "7.3.6",
      "category": "UI Components",
      "frameworkSpecific": true,
      "source": "package.json",
      "usage": {
        "importCount": 1,
        "importLocations": [
          "src/Components/sidebar/Profile.jsx"
        ],
        "components": [
          "Icon"
        ],
        "features": [
          "Material Design SVG icons"
        ]
      },
      "importPattern": "import IconName from '@mui/icons-material/IconName'",
      "alternatives": [
        "react-icons"
      ],
      "legacyPattern": "",
      "website": "https://mui.com/material-ui/material-icons/",
      "documentation": "https://mui.com/material-ui/material-icons/"
    },
    {
      "name": "@emotion/react",
      "version": "11.14.0",
      "category": "Styling",
      "frameworkSpecific": true,
      "source": "package.json",
      "usage": {
        "importCount": 2,
        "importLocations": [
          "src/App.jsx",
          "src/Components/sidebar/Profile.jsx"
        ],
        "components": [
          "ThemeProvider",
          "css"
        ],
        "features": [
          "CSS-in-JS styling"
        ]
      },
      "importPattern": "import { css } from '@emotion/react'",
      "alternatives": [
        "styled-components"
      ],
      "legacyPattern": "",
      "website": "https://emotion.sh/docs/@emotion/react",
      "documentation": "https://emotion.sh/docs/@emotion/react"
    },
    {
      "name": "@emotion/styled",
      "version": "11.14.1",
      "category": "Styling",
      "frameworkSpecific": true,
      "source": "package.json",
      "usage": {
        "importCount": 2,
        "importLocations": [
          "src/App.jsx",
          "src/Components/sidebar/Profile.jsx"
        ],
        "components": [
          "styled"
        ],
        "features": [
          "Styled components"
        ]
      },
      "importPattern": "import styled from '@emotion/styled'",
      "alternatives": [
        "styled-components"
      ],
      "legacyPattern": "",
      "website": "https://emotion.sh/docs/styled",
      "documentation": "https://emotion.sh/docs/styled"
    }
  ],
  "developmentDependencies": [
    {
      "name": "vite",
      "version": "7.3.0",
      "purpose": "Build tool and development server",
      "buildTool": "vite",
      "configFiles": [
        "vite.config.js"
      ]
    },
    {
      "name": "@vitejs/plugin-react",
      "version": "5.1.2",
      "purpose": "React fast refresh and JSX transform for Vite",
      "buildTool": "vite",
      "configFiles": [
        "vite.config.js"
      ]
    },
    {
      "name": "eslint",
      "version": "9.39.2",
      "purpose": "Linting JavaScript/JSX code",
      "buildTool": "eslint",
      "configFiles": [
        "eslint.config.js"
      ]
    },
    {
      "name": "@eslint/js",
      "version": "9.39.2",
      "purpose": "ESLint base rules",
      "buildTool": "eslint",
      "configFiles": [
        "eslint.config.js"
      ]
    },
    {
      "name": "eslint-plugin-react-hooks",
      "version": "7.0.1",
      "purpose": "ESLint rules for React hooks",
      "buildTool": "eslint",
      "configFiles": [
        "eslint.config.js"
      ]
    },
    {
      "name": "eslint-plugin-react-refresh",
      "version": "0.4.26",
      "purpose": "ESLint rules for React Fast Refresh",
      "buildTool": "eslint",
      "configFiles": [
        "eslint.config.js"
      ]
    },
    {
      "name": "globals",
      "version": "16.5.0",
      "purpose": "Global variable definitions for ESLint",
      "buildTool": "eslint",
      "configFiles": [
        "eslint.config.js"
      ]
    },
    {
      "name": "@types/react",
      "version": "19.2.7",
      "purpose": "TypeScript type definitions for React (for IDE support)",
      "buildTool": "none",
      "configFiles": []
    },
    {
      "name": "@types/react-dom",
      "version": "19.2.3",
      "purpose": "TypeScript type definitions for ReactDOM (for IDE support)",
      "buildTool": "none",
      "configFiles": []
    }
  ],
  "frameworkSpecificLibraries": [
    {
      "name": "@mui/material",
      "version": "7.3.6",
      "frameworkName": "React",
      "purpose": "Material Design UI components for React",
      "components": [
        "Button",
        "Typography",
        "Box",
        "Stack",
        "Paper",
        "Avatar"
      ]
    },
    {
      "name": "@mui/icons-material",
      "version": "7.3.6",
      "frameworkName": "React",
      "purpose": "Material Design SVG icons for React",
      "components": [
        "Icon"
      ]
    },
    {
      "name": "@emotion/react",
      "version": "11.14.0",
      "frameworkName": "React",
      "purpose": "CSS-in-JS styling for React components",
      "components": [
        "ThemeProvider",
        "css"
      ]
    },
    {
      "name": "@emotion/styled",
      "version": "11.14.1",
      "frameworkName": "React",
      "purpose": "Styled components for React",
      "components": [
        "styled"
      ]
    }
  ],
  "cdnResources": [],
  "legacyDependencies": [],
  "potentiallyUnusedDependencies": [],
  "dependencyIssues": [],
  "analysis": {
    "timestamp": "2024-06-13T12:10:00Z",
    "processingTimeMs": 3500
  },
  "errors": [],
  "summary": "This modern React (19.x) application uses Vite as its build tool and leverages Material-UI (MUI) and Emotion for UI and styling. All runtime dependencies are directly used in the codebase, with no legacy or CDN-based dependencies detected. Development dependencies are focused on linting, build, and IDE support. No version conflicts, deprecated, or unused dependencies were found. The dependency map is comprehensive and ready for further workflow processing."
}