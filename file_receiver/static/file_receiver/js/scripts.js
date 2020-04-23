document.querySelector('button#modal-upload-btn').addEventListener('click', () => {
    let formElement = document.querySelector('div.modal-body form');
    let formData = new FormData(formElement);

    let xhr = new XMLHttpRequest();

    let progressBar = document.querySelector('div.progress-bar');

    let uploadBtn = document.querySelector('button#modal-upload-btn');
    uploadBtn.setAttribute("disabled", "");

    xhr.onreadystatechange = () => {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            console.log(xhr.responseText);
            uploadBtn.removeAttribute('disabled');
            progressBar.setAttribute('aria-valuenow', 0);
            progressBar.style.width = '0%';
            progressBar.textContent = '';
            let redirectTo = 'http://' + HOSTNAME + RESTfulAPI_URLS.file_list;
            window.location.replace(redirectTo);
        } else {
            console.log(xhr.readyState);
        }
    };

    xhr.upload.addEventListener('progress', (progressEvent) => {

        if (progressEvent.lengthComputable) {
            let p = (progressEvent.loaded / progressEvent.total) * 100;
            console.log(progressEvent.loaded);
            console.log(progressEvent.total);
            console.log(p);
            progressBar.setAttribute('aria-valuenow', p.toPrecision(3));
            progressBar.style.width = `${p.toPrecision(3)}%`;
            progressBar.textContent = `${p.toPrecision(3)}%`;
        }
    });

    xhr.open('POST', formElement.action);

    xhr.send(formData);
});