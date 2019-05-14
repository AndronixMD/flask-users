var buttonsDelete = document.querySelectorAll('.button.is-danger');
var modal = document.querySelector('.modal');

if (buttonsDelete) {
  var buttonsClose = modal.querySelectorAll('.cancel');
  var buttonConfirm = modal.querySelector('.confirm');
  var userId = null;

  for (var i = 0; i < buttonsDelete.length; i++) {
    buttonsDelete[i].addEventListener('click', function () {
      modal.classList.add('is-active');
      userId = this.dataset.userid;
    });
  }

  for (var i = 0; i < buttonsClose.length; i++) {
    buttonsClose[i].addEventListener('click', function () {
      modal.classList.remove('is-active');
    });
  }

  buttonConfirm.addEventListener('click', function () {
    var url = location.origin + '/?user_id=' + userId;
    fetch(url, {
        method: 'DELETE'
      })
      .then(() => window.location = '/');
    // window.location = '/';
  });
}