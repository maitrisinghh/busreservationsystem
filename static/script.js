
document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');

    
    form.addEventListener('submit', function (e) {
       
        e.preventDefault();

       
        const name = document.querySelector('[name="name"]').value;
        const email = document.querySelector('[name="email"]').value;
        const phone = document.querySelector('[name="phone"]').value;
        const origin = document.querySelector('[name="origin"]').value;
        const destination = document.querySelector('[name="destination"]').value;
        const date = document.querySelector('[name="date"]').value;
        const seats = document.querySelector('[name="seats"]').value;

        
        if (!name || !email || !phone || !origin || !destination || !date || !seats) {
            alert("Please fill in all the fields.");
            return;
        }

        
        
    });
});
