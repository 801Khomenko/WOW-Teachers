let admin = prompt('Кто пришел?');

if (admin == "Отмена"){
    close.prompt
}else if (admin == "Админ") {
    let password = prompt('Пароль?');
    if (password == "Админ"){
        alert("Привет чувырло!");
    
    } else if (password == "Отмена"){
        close.prompt;
    } else{
        alert("Пароль неверен")
    }
} else{
    alert("Я вас не знаю");
}

