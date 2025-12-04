// Client-side helpers for dynamic template manipulation (if used in browser)
function updatePlaceholder(selector, value) {
  document.querySelector(selector).textContent = value;
}

// Example: updatePlaceholder('.student-name', 'John Doe');
