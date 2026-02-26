document.addEventListener('DOMContentLoaded', function() {
    // Django modelindeki alan adlarına göre (genelde id_alanadi olur)
    // Eğer içeriği 'content' alanından alıyorsan:
    const contentInput = document.querySelector('#id_content') || document.querySelector('#id_text') || document.querySelector('textarea');
    const previewText = document.querySelector('#preview-text');

    if (contentInput && previewText) {
        contentInput.addEventListener('input', function() {
            // Yazılan metni sağdaki karta aktar
            previewText.innerText = this.value;
            
            // Eğer boşsa varsayılan metni göster
            if (this.value.trim() === "") {
                previewText.innerText = "Formu doldurmaya başlayın...";
            }
        });
    }
});