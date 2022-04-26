function getValue(value) {
    if (value === '---') {
        //alert(value);
        document.img.src = '/static/img/main_reservation.webp'; // стоковое изображение из html
    } else if (value === 'Одноместный номер') {
        document.img.src = '/static/img/overlook.jpg';
    } else if (value === 'Двухместный номер') {
        document.img.src = '/static/img/overlook_2.jpg';
    }
}