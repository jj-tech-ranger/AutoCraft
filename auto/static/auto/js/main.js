// AutoCraft Main JavaScript
document.addEventListener('DOMContentLoaded', function() {
    console.log('AutoCraft loaded successfully');
    
    // Auto-hide messages after 5 seconds
    const messages = document.querySelectorAll('.alert');
    if (messages.length > 0) {
        setTimeout(function() {
            messages.forEach(function(message) {
                message.style.transition = 'opacity 0.5s';
                message.style.opacity = '0';
                setTimeout(function() {
                    message.remove();
                }, 500);
            });
        }, 5000);
    }
    
    // Confirm delete actions
    const deleteButtons = document.querySelectorAll('.btn-delete');
    deleteButtons.forEach(function(button) {
        button.addEventListener('click', function(e) {
            if (!confirm('Are you sure you want to delete this item?')) {
                e.preventDefault();
            }
        });
    });
    
    // Form validation
    const forms = document.querySelectorAll('form');
    forms.forEach(function(form) {
        form.addEventListener('submit', function(e) {
            const requiredFields = form.querySelectorAll('[required]');
            let isValid = true;
            
            requiredFields.forEach(function(field) {
                if (!field.value.trim()) {
                    isValid = false;
                    field.style.borderColor = '#dc3545';
                } else {
                    field.style.borderColor = '';
                }
            });
            
            if (!isValid) {
                e.preventDefault();
                alert('Please fill in all required fields');
            }
        });
    });
    
    // Table row highlighting
    const tableRows = document.querySelectorAll('.data-table tbody tr');
    tableRows.forEach(function(row) {
        row.addEventListener('click', function() {
            tableRows.forEach(function(r) {
                r.style.backgroundColor = '';
            });
            this.style.backgroundColor = '#e9ecef';
        });
    });
});
