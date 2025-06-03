# Troubleshooting Guide

## Local Server Issues

This document provides solutions for common issues encountered when running the portfolio website locally.

### Problem: Server Shows Directory Listing Instead of Website

**Symptoms:**
- Running `python3 -m http.server` shows the home directory listing instead of the website
- 404 errors when trying to access `index.html`
- Server serves from wrong directory despite being in the project folder

### Solutions (In Order of Preference)

#### Solution 1: Direct File Opening (Recommended)
Open the HTML file directly in your browser:
```bash
open /Users/cooperpenniman/Documents/personal-website/index.html
```
Or use the generic path:
```bash
open index.html
```

**Pros:** Bypasses server issues entirely, works immediately, no port conflicts

#### Solution 2: Kill processes and restart server
```bash
pkill -f "python.*http.server" 2>/dev/null; sleep 1; python3 -m http.server 8000
```

#### Solution 3: Use alternative ports
```bash
python3 -m http.server 3001
python3 -m http.server 3002
```

### Common Error Messages
- "Address already in use" - Another server is running on that port
- "404 File not found" for index.html - Server serving from wrong directory
- Directory listing instead of website - Server defaulting to home directory

### Debugging Tips
1. Verify you're in the correct directory: `pwd`
2. Check if index.html exists: `ls -la index.html`
3. Kill all Python processes: `killall python3`
4. Find what's using a port: `lsof -i :8000`

---
**Last Updated:** June 3, 2025
**Issue Resolved:** Direct file opening method successfully deployed
**Note:** This issue appears to be macOS-specific related to Python HTTP server directory handling
