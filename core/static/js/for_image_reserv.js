function getValue(value) {
    if (value === '---') {
        //alert(value);
        document.img.src = '/static/img/main_reservation.webp'; // стоковое изображение из html
    } else {
        document.img.src = value;
    }
}