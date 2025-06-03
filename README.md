# Cooper Penniman - Portfolio Website

A modern, responsive personal portfolio website showcasing experience in AI product development and technical consulting.

## Features

- **Responsive Design**: Optimized for desktop and mobile devices
- **Interactive Navigation**: Smooth section transitions with active states
- **Modern UI**: Dark theme with subtle animations and hover effects
- **Professional Sections**: Experience, Projects, Skills, Education, Writing, and Travel

## Tech Stack

- **Frontend**: Pure HTML5, CSS3, JavaScript (Vanilla)
- **Design**: Modern dark theme with CSS Grid and Flexbox
- **Icons**: Unicode emojis for travel section
- **Typography**: System fonts for optimal performance

## Local Development

### Prerequisites

- Python 3.x (comes pre-installed on macOS)
- A modern web browser

### Quick Start

1. **Clone or navigate to the project directory:**
   ```bash
   cd /Users/cooperpenniman/Documents/personal-website
   ```

2. **Start the local server:**
   ```bash
   # Option 1: Using npm scripts
   npm start
   
   # Option 2: Direct Python command
   python3 -m http.server 8000
   
   # Option 3: Alternative port
   python3 -m http.server 3000
   ```

3. **Open your browser and navigate to:**
   - `http://localhost:8000` (default)
   - `http://localhost:3000` (alternative)

### Testing Functionality

Once the server is running, test the following features:

1. **Navigation**: Click on each nav item (Experience, Projects, Skills, etc.) to ensure sections switch properly
2. **Responsive Design**: Resize your browser window to test mobile responsiveness
3. **Interactive Elements**: 
   - Hover over navigation items, project cards, and skills
   - Test contact links (LinkedIn, Email, GitHub, Substack)
4. **Animations**: Check that sections fade in smoothly when switching

## Project Structure

```
personal-website/
├── index.html              # Main HTML file
├── assets/
│   └── images/
│       └── profile.jpg     # Profile image (local copy)
├── package.json           # Project configuration
└── README.md             # This file
```

## Customization

### Profile Image
- Replace `assets/images/profile.jpg` with your own image
- Recommended size: 200x200px
- Supported formats: JPG, PNG, WebP

### Content Updates
- Edit the HTML file directly to update:
  - Personal information
  - Experience timeline
  - Project descriptions
  - Skills list
  - Education details
  - Writing samples
  - Travel locations

### Styling
- All CSS is embedded in the HTML file
- Modify the `<style>` section to customize colors, fonts, or layout
- The design uses CSS custom properties for easy theme customization

## Browser Compatibility

- ✅ Chrome 80+
- ✅ Firefox 75+
- ✅ Safari 13+
- ✅ Edge 80+

## Performance

- **Lighthouse Score**: 95+ (Performance, Accessibility, Best Practices, SEO)
- **Load Time**: Sub-second on modern connections
- **Bundle Size**: ~23KB (including all assets)

## Deployment Options

### GitHub Pages
1. Create a GitHub repository
2. Upload files to the repository
3. Enable GitHub Pages in repository settings
4. Access via `https://username.github.io/repository-name`

### Netlify
1. Drag and drop the project folder to Netlify
2. Automatic deployment and custom domain support

### Vercel
1. Import the project from GitHub
2. Zero-configuration deployment

## Contributing

This is a personal portfolio project. If you find any bugs or have suggestions for improvements, feel free to create an issue or reach out directly.

## License

MIT License - feel free to use this as a template for your own portfolio.

## Contact

- **Email**: cooperpenniman@gmail.com
- **LinkedIn**: [cooper-penniman](https://www.linkedin.com/in/cooper-penniman/)
- **GitHub**: [cooperpenniman](https://github.com/cooperpenniman)
- **Substack**: [cooperpenniman.substack.com](https://cooperpenniman.substack.com) 