/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: ["class"],
  content: [
    './pages/**/*.{ts,tsx,vue}',
    './components/**/*.{ts,tsx,vue}',
    './app/**/*.{ts,tsx,vue}',
    './src/**/*.{ts,tsx,vue}',
  ],
  theme: {
    container: {
      center: true,
      padding: "2rem",
      screens: {
        "2xl": "1400px",
      },
    },
    extend: {
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
      },
      colors: {
        border: "#cbc4d2", // outline-variant
        input: "#cbc4d2",
        ring: "#4f378a", // primary
        background: "#fdf7ff",
        foreground: "#1d1b20",
        primary: {
          DEFAULT: "#4f378a",
          foreground: "#ffffff",
          container: "#6750a4",
        },
        secondary: {
          DEFAULT: "#63597c",
          foreground: "#ffffff",
        },
        destructive: {
          DEFAULT: "#ba1a1a",
          foreground: "#ffffff",
        },
        muted: {
          DEFAULT: "#f2ecf4", // surface-container
          foreground: "#494551", // on-surface-variant
        },
        accent: {
          DEFAULT: "#e1d4fd", // secondary-container
          foreground: "#645a7d",
        },
        popover: {
          DEFAULT: "#ffffff",
          foreground: "#1d1b20",
        },
        card: {
          DEFAULT: "#ffffff",
          foreground: "#1d1b20",
        },
        // Stitch custom colors
        "primary-fixed": "#e9ddff",
        "secondary-fixed-dim": "#cdc0e9",
        "tertiary-container": "#c9a74d",
        "tertiary-fixed-dim": "#e7c365",
        "surface-container-highest": "#e6e0e9",
        "tertiary-fixed": "#ffdf93",
        "surface-container-low": "#f8f2fa",
        "surface-tint": "#6750a4",
        "on-primary": "#ffffff",
        "inverse-surface": "#322f35",
        "surface-container-lowest": "#ffffff",
        "surface-variant": "#e6e0e9",
        "on-error": "#ffffff",
        "on-secondary-container": "#645a7d",
        "primary-fixed-dim": "#cfbcff",
        "on-tertiary-container": "#503d00",
        "surface-container": "#f2ecf4",
        "on-primary-fixed": "#22005d",
        "inverse-on-surface": "#f5eff7",
        "on-primary-container": "#e0d2ff",
        "on-surface": "#1d1b20",
        "secondary-container": "#e1d4fd",
        "on-secondary": "#ffffff",
        "on-tertiary": "#ffffff",
        "primary-container": "#6750a4",
        "surface-container-high": "#ece6ee",
        "outline": "#7a7582",
        "secondary-fixed": "#e9ddff",
        "error-container": "#ffdad6",
        "on-secondary-fixed-variant": "#4b4263",
        "tertiary": "#765b00",
        "surface-bright": "#fdf7ff",
        "inverse-primary": "#cfbcff",
        "on-surface-variant": "#494551",
        "error": "#ba1a1a",
        "on-error-container": "#93000a",
        "surface": "#fdf7ff",
        "outline-variant": "#cbc4d2",
        "on-tertiary-fixed-variant": "#594400",
        "on-primary-fixed-variant": "#4f378a",
        "on-secondary-fixed": "#1f1635",
        "surface-dim": "#ded8e0",
        "on-tertiary-fixed": "#241a00",
        "on-background": "#1d1b20"
      },
      borderRadius: {
        lg: "12px",
        md: "8px",
        sm: "4px",
      },
      spacing: {
        "sm": "8px",
        "xl": "32px",
        "container_max": "1200px",
        "xs": "4px",
        "base": "8px",
        "2xl": "48px",
        "3xl": "64px",
        "md": "16px",
        "gutter": "24px",
        "lg": "24px"
      },
      fontSize: {
        "body-md": ["16px", {"lineHeight": "1.5", "fontWeight": "400"}],
        "headline-md": ["24px", {"lineHeight": "1.3", "fontWeight": "600"}],
        "display": ["48px", {"lineHeight": "1.1", "letterSpacing": "-0.02em", "fontWeight": "700"}],
        "body-sm": ["14px", {"lineHeight": "1.5", "fontWeight": "400"}],
        "headline-sm": ["18px", {"lineHeight": "1.4", "fontWeight": "600"}],
        "label-md": ["14px", {"lineHeight": "1", "letterSpacing": "0.01em", "fontWeight": "600"}],
        "body-lg": ["18px", {"lineHeight": "1.6", "fontWeight": "400"}],
        "label-sm": ["12px", {"lineHeight": "1", "fontWeight": "500"}],
        "headline-lg-mobile": ["24px", {"lineHeight": "1.25", "fontWeight": "600"}],
        "headline-lg": ["32px", {"lineHeight": "1.25", "letterSpacing": "-0.02em", "fontWeight": "600"}]
      },
      keyframes: {
        "accordion-down": {
          from: { height: 0 },
          to: { height: "var(--radix-accordion-content-height)" },
        },
        "accordion-up": {
          from: { height: "var(--radix-accordion-content-height)" },
          to: { height: 0 },
        },
      },
      animation: {
        "accordion-down": "accordion-down 0.2s ease-out",
        "accordion-up": "accordion-up 0.2s ease-out",
      },
    },
  },
  plugins: [],
}
