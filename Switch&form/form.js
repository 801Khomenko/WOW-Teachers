window.onload = function(){
    let btn = document.querySelector('.submit');
    
    function stop(event){
        event.preventDefault();
    }

    btn.addEventListener('click', stop, false);

    btn.addEventListener('click', function(){
        let form = document.querySelector('#modal_form');
        let overlay = document.querySelector('#overlay');

        form.style.display = 'block';
    })
}