const usernameField = document.querySelector("#username");
const usernameFeedBackAreaInvalid = document.querySelector(".usernameFeedbackArea1");
const usernameFeedBackAreaValid = document.querySelector(".usernameFeedbackArea2");
const emailField = document.querySelector("#email");
const emailFeedBackAreaInvalid = document.querySelector(".emailFeedbackArea1");
const emailFeedBackAreaValid = document.querySelector(".emailFeedbackArea2");
const submitBtn = document.querySelector(".btn");

usernameField.addEventListener("keyup", (e) => {
    const usernameVal = e.target.value;

    if (usernameVal.length > 0) {
      fetch("/auth/validate_username/", {
        body: JSON.stringify({ username: usernameVal }),
        method: "POST",
      })
        .then((res) => res.json())
        .then((data) => {
          if (data.username_error) {
            submitBtn.disabled = true;
            usernameField.classList.remove("is-valid");
            usernameFeedBackAreaValid.style.display = "none";
            usernameField.classList.add("is-invalid");
            usernameFeedBackAreaInvalid.style.display = "block";
            usernameFeedBackAreaInvalid.innerHTML = `<p>${data.username_error}</p>`;
          } else {
            submitBtn.removeAttribute("disabled");
            usernameField.classList.remove("is-invalid");
            usernameFeedBackAreaInvalid.style.display = "none";
            usernameField.classList.add("is-valid");
            usernameFeedBackAreaValid.style.display = "block";
            usernameFeedBackAreaValid.innerHTML = `<p>Tersedia</p>`;
          }
        });
    } else {
      fetch("/auth/validate_username/", {
        body: JSON.stringify({ username: usernameVal }),
        method: "POST",
      })
      .then((res) => res.json())
      .then((data) => {
        console.log("data", data);
        usernameField.classList.remove("is-invalid");
        usernameFeedBackAreaInvalid.style.display = "none";
        usernameField.classList.remove("is-valid");
        usernameFeedBackAreaValid.style.display = "none";
      });
    }
  });

emailField.addEventListener("keyup", (e) => {
    const emailVal = e.target.value;
  
    if (emailVal.length > 0) {
      fetch("/auth/validate_email/", {
        body: JSON.stringify({ email: emailVal }),
        method: "POST",
      })
        .then((res) => res.json())
        .then((data) => {
          console.log("data", data);
          if (data.email_error) {
            submitBtn.disabled = true;
            emailField.classList.remove("is-valid");
            emailFeedBackAreaValid.style.display = "none";
            emailField.classList.add("is-invalid");
            emailFeedBackAreaInvalid.style.display = "block";
            emailFeedBackAreaInvalid.innerHTML = `<p>${data.email_error}</p>`;
          } else {
            submitBtn.removeAttribute("disabled");
            emailField.classList.remove("is-invalid");
            emailFeedBackAreaInvalid.style.display = "none";
            emailField.classList.add("is-valid");
            emailFeedBackAreaValid.style.display = "block";
            emailFeedBackAreaValid.innerHTML = `<p>Tersedia</p>`;
          }
        });
    } else {
      fetch("/auth/validate_email/", {
        body: JSON.stringify({ email: emailVal }),
        method: "POST",
      })
      .then((res) => res.json())
      .then((data) => {
        console.log("data", data);
        emailField.classList.remove("is-invalid");
        emailFeedBackAreaInvalid.style.display = "none";
        emailField.classList.remove("is-valid");
        emailFeedBackAreaValid.style.display = "none";
      });
    }
  });