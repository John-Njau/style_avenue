<template>
  <div class="sign-up w-50 m-auto">
    <section class="h-100 h-custom">
      <div class="container py-5 h-100">
        <div class="row d-flex justify-content-center align-items-center h-100">
          <div class="col-lg-8 col-xl-6">
            <div class="card rounded-3 signin-card">
              <img
                src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-registration/img3.webp"
                class="w-100"
                style="
                  border-top-left-radius: 0.3rem;
                  border-top-right-radius: 0.3rem;
                "
                alt="Sample photo"
              />
              <div class="card-body p-2 p-md-5">
                <p class="text-center h3 fw-bold mb-5 mx-1 mx-md-4 mt-3">
                  Sign up
                </p>

                <form class="px-md-2">
                  <div class="form-outline mb-2">
                    <input
                      type="text"
                      id="form3Example1q"
                      class="form-control"
                      placeholder="Your Name"
                    />
                  </div>

                  <div class="">
                    <div class="">
                      <div class="form-outline mb-2">
                        <input
                          type="email"
                          id="form3Example1w"
                          class="form-control"
                          placeholder="Your Email"
                        />
                      </div>
                    </div>
                  </div>

                  <div class="">
                    <div class="">
                      <div class="form-outline mb-2">
                        <input
                          type="Password"
                          id="form3Example1w"
                          class="form-control"
                          placeholder="Password"
                        />
                      </div>
                    </div>
                  </div>
                  <div class="">
                    <div class="">
                      <div class="form-outline mb-2">
                        <input
                          type="Password"
                          id="form3Example1w"
                          class="form-control"
                          placeholder="Confirm Password"
                        />
                      </div>
                    </div>
                  </div>

                  <button type="submit" class="btn btn-primary btn-sm mb-1">
                    Submit
                  </button>
                  <p>
                    Already have an account?
                    <a href="/signIn">Sign in</a>
                  </p>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {};
</script>

<style>
.signin-card {
  box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.402);
  background-color: antiquewhite !important;
}
</style>