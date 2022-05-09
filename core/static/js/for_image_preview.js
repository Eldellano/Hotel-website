function getValue(src) {
    //alert(src.substr(src.indexOf('/static'),[src.length]))
    let image = src.substr(src.indexOf('/static'), [src.length]);
    document.img_active.src = image;
    document.img_item.src = image;
}
