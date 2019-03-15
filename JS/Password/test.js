let admin = prompt('Кто пришел?');

if (admin == null){
    alert("Вход отменен!");
}else if (admin == "Админ") {
    let password = prompt('Пароль?');
    if (password == "Админ"){
        alert("Привет чувырло!");
    
    } else if (password == null){
        close.prompt;
    } else{
        alert("Пароль неверен")
    }
}else if(admin="Хуило")  {
    alert("Сам такий")  
} else{
    alert("Я вас не знаю");
}

