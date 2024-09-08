
# Interactive Map Project

## Current Status:
- **U.S. map SVG**: The U.S. map has been downloaded, but it hasn't been embedded into the HTML yet.
- **Map interaction**: The decision has been made to embed the SVG directly into the HTML for better control, with plans to load maps dynamically as external files for scalability.
- **JavaScript interaction**: A basic concept of interacting with individual states (clicks, popups, custom background image uploads) has been planned.
- **Multiple maps planned**: There are plans to add U.S. national parks and world maps as options.
- **Pop-up confirmation**: A popup to confirm state selection and avoid accidental clicks has been outlined.
- **Future mobile version**: Plans have been mentioned for a mobile version, but no specific work has started on this.

## Todos:

### Immediate Tasks:
1. **Embed the U.S. SVG map** into the HTML for interactive control.
2. **Implement state interactivity**:
   - Make states clickable.
   - Show a confirmation popup when a state is clicked.
   - Mark a state as "visited" with a background image or color change upon confirmation.
3. **Set up dynamic loading for multiple maps**:
   - U.S. map
   - World map
   - U.S. national parks map
4. **Add support for custom background images**:
   - Allow users to upload their own images for visited states or locations during the confirmation step.
5. **Set up basic user authentication**:
   - Create a login system so users can log in and track their visited states.

### Future/Long-Term Tasks:
6. **Mobile compatibility**:
   - Ensure the layout is responsive for future mobile app development.
7. **Expand map options**:
   - Add more maps (e.g., world, parks) and ensure scalability.
8. **User data persistence**:
   - Save visited states and uploaded images in a backend database.
9. **Build the mobile app version** based on the website.
