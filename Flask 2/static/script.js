// Обработка загрузки изображения
document.getElementById('imageUpload').addEventListener('change', function(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const img = document.getElementById('uploadedImage');
            img.src = e.target.result;
            img.style.display = 'block'; // Показываем изображение

            // Скрываем кнопку загрузки и изображения на выбор
            document.querySelector('.custom-file-upload').style.display = 'none';
            document.getElementById('imageOptions').style.display = 'none';

            // Показываем текстовые поля, радио-кнопки и поле для размера шрифта
            document.querySelectorAll('.text-input').forEach(input => input.style.display = 'inline-block');
            document.querySelector('.font-selector').style.display = 'block';
            document.querySelector('.font-size-selector').style.display = 'block';

            // Отрисовываем мем на canvas
            drawMeme();

            // Показываем кнопку скачивания
            document.getElementById('downloadButton').style.display = 'block';
        }
        reader.readAsDataURL(file);
    }
});

// Выбор изображения из предложенных
function selectImage(image) {
    const img = document.getElementById('uploadedImage');
    img.src = image.src;
    img.style.display = 'block'; // Показываем выбранное изображение

    // Скрываем кнопку загрузки и изображения на выбор
    document.querySelector('.custom-file-upload').style.display = 'none';
    document.getElementById('imageOptions').style.display = 'none';

    // Показываем текстовые поля, радио-кнопки и поле для размера шрифта
    document.querySelectorAll('.text-input').forEach(input => input.style.display = 'inline-block');
    document.querySelector('.font-selector').style.display = 'block';
    document.querySelector('.font-size-selector').style.display = 'block';

    // Отрисовываем мем на canvas
    drawMeme();

    // Показываем кнопку скачивания
    document.getElementById('downloadButton').style.display = 'block';
}

// Обновление текста сверху
document.getElementById('topTextInput').addEventListener('input', function() {
    document.getElementById('textTop').textContent = this.value;
    drawMeme();
});

// Обновление текста снизу
document.getElementById('bottomTextInput').addEventListener('input', function() {
    document.getElementById('textBottom').textContent = this.value;
    drawMeme();
});

// Изменение шрифта текста на картинке
document.querySelectorAll('input[name="font"]').forEach(radio => {
    radio.addEventListener('change', function() {
        const textTop = document.getElementById('textTop');
        const textBottom = document.getElementById('textBottom');

        if (this.value === 'impact') {
            textTop.style.fontFamily = 'Impact, sans-serif';
            textTop.style.webkitTextStroke = '1.5px black';
            textBottom.style.fontFamily = 'Impact, sans-serif';
            textBottom.style.webkitTextStroke = '1.5px black';
        } else if (this.value === 'lobster') {
            textTop.style.fontFamily = '"Lobster", sans-serif';
            textTop.style.webkitTextStroke = '0px';
            textBottom.style.fontFamily = '"Lobster", sans-serif';
            textBottom.style.webkitTextStroke = '0px';
        }

        drawMeme();
    });
});

// Изменение размера шрифта
document.getElementById('fontSize').addEventListener('input', function() {
    const fontSize = this.value + 'px';
    document.getElementById('textTop').style.fontSize = fontSize;
    document.getElementById('textBottom').style.fontSize = fontSize;
    drawMeme();
});

// Обработка вставки изображения через Ctrl + V
document.addEventListener('paste', function(event) {
    const items = (event.clipboardData || event.originalEvent.clipboardData).items;

    for (let item of items) {
        if (item.kind === 'file' && item.type.startsWith('image/')) {
            const file = item.getAsFile();
            const reader = new FileReader();

            reader.onload = function(e) {
                const img = document.getElementById('uploadedImage');
                img.src = e.target.result;
                img.style.display = 'block'; // Показываем изображение

                // Скрываем кнопку загрузки и изображения на выбор
                document.querySelector('.custom-file-upload').style.display = 'none';
                document.getElementById('imageOptions').style.display = 'none';

                // Показываем текстовые поля, радио-кнопки и поле для размера шрифта
                document.querySelectorAll('.text-input').forEach(input => input.style.display = 'inline-block');
                document.querySelector('.font-selector').style.display = 'block';
                document.querySelector('.font-size-selector').style.display = 'block';

                // Отрисовываем мем на canvas
                drawMeme();

                // Показываем кнопку скачивания
                document.getElementById('downloadButton').style.display = 'block';

                // Показываем сообщение о вставке
                const pasteMessage = document.getElementById('pasteMessage');
                pasteMessage.style.display = 'block';
                setTimeout(() => {
                    pasteMessage.style.display = 'none';
                }, 3000); // Скрываем сообщение через 3 секунды
            };

            reader.readAsDataURL(file);
            break; // Прерываем цикл, если нашли изображение
        }
    }
});

// Функция для отрисовки изображения и текста на canvas
function drawMeme() {
    const canvas = document.getElementById('memeCanvas');
    const ctx = canvas.getContext('2d');

    const img = document.getElementById('uploadedImage');
    const textTop = document.getElementById('textTop').textContent;
    const textBottom = document.getElementById('textBottom').textContent;

    // Устанавливаем размеры canvas равными размерам изображения
    canvas.width = img.width;
    canvas.height = img.height;

    // Отрисовываем изображение на canvas
    ctx.drawImage(img, 0, 0, canvas.width, canvas.height);

    // Настройки шрифта для текста
    const fontSize = document.getElementById('fontSize').value + 'px';
    const fontFamily = document.querySelector('input[name="font"]:checked').value === 'impact' ? 'Impact' : 'Lobster';
    ctx.font = `${fontSize} ${fontFamily}`;
    ctx.fillStyle = 'white';
    ctx.strokeStyle = 'black';
    ctx.lineWidth = 2;
    ctx.textAlign = 'center';

    // Отрисовываем текст сверху
    ctx.strokeText(textTop, canvas.width / 2, 60);
    ctx.fillText(textTop, canvas.width / 2, 60);

    // Отрисовываем текст снизу
    ctx.strokeText(textBottom, canvas.width / 2, canvas.height - 20);
    ctx.fillText(textBottom, canvas.width / 2, canvas.height - 20);
}

// Функция для скачивания итоговой картинки
function downloadMeme() {
    const canvas = document.getElementById('memeCanvas');
    const link = document.createElement('a');
    link.href = canvas.toDataURL('image/png'); // Преобразуем canvas в PNG
    link.download = 'meme.png'; // Имя файла для скачивания
    link.click();
}

// Обработчик для кнопки скачивания
document.getElementById('downloadButton').addEventListener('click', downloadMeme);