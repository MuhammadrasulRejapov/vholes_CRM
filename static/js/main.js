// Main JavaScript for Fashion Dashboard

document.addEventListener("DOMContentLoaded", () => {
  // Initialize tooltips
  var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
  var tooltipList = tooltipTriggerList.map((tooltipTriggerEl) => new window.bootstrap.Tooltip(tooltipTriggerEl))

  // Auto-dismiss alerts after 5 seconds
  setTimeout(() => {
    var alerts = document.querySelectorAll(".alert")
    alerts.forEach((alert) => {
      var bsAlert = new window.bootstrap.Alert(alert)
      bsAlert.close()
    })
  }, 5000)

  // Preview image before upload
  const imageInput = document.querySelector('input[type="file"][name="image"]')
  if (imageInput) {
    imageInput.addEventListener("change", function () {
      const file = this.files[0]
      if (file) {
        const reader = new FileReader()
        reader.onload = (e) => {
          // Check if there's an existing preview
          let preview = document.querySelector(".image-preview")
          if (!preview) {
            // Create preview element if it doesn't exist
            preview = document.createElement("div")
            preview.className = "image-preview mt-2"
            preview.innerHTML =
              '<p>Preview:</p><img src="/placeholder.svg" class="img-thumbnail" style="max-height: 150px;">'
            imageInput.parentNode.appendChild(preview)
          }
          // Update the preview image
          preview.querySelector("img").src = e.target.result
        }
        reader.readAsDataURL(file)
      }
    })
  }

  // Confirm delete actions
  const deleteButtons = document.querySelectorAll('.btn-danger:not([type="submit"])')
  deleteButtons.forEach((button) => {
    if (!button.closest("form")) {
      // Skip buttons inside forms
      button.addEventListener("click", (e) => {
        if (!confirm("Are you sure you want to delete this item? This action cannot be undone.")) {
          e.preventDefault()
        }
      })
    }
  })

  // Highlight low stock items
  const stockCells = document.querySelectorAll("td:nth-child(5)")
  stockCells.forEach((cell) => {
    const stockText = cell.textContent.trim()
    if (stockText.includes("Low")) {
      cell.closest("tr").classList.add("table-danger")
    }
  })
})
