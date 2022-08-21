<template>
  <div class="sign-in w-50 m-auto mt-5">
    <form class="form-signin w-50 m-auto card p-2" >
      <div class="text-center mb-4">
        <img
          class="mb-4"
          src="../../assets/images/style_avenue_logo.jpg"
          alt=""
          width="72"
          height="72"
        />
        <h1 class="h3 mb-3 font-weight-bold">Style Avenue Studio</h1>
      </div>

      <div class="form-label-group m-2">
        <input
          type="email"
          id="inputEmail"
          class="form-control"
          placeholder="Email address"
          required
          autofocus
        />
      </div>

      <div class="form-label-group m-2">
        <input
          type="password"
          id="inputPassword"
          class="form-control"
          placeholder="Password"
          required
        />
      </div>

      <!-- <div class="checkbox mb-3">
        <label>
          <small>
            <input type="checkbox" value="remember-me" /> Remember me
          </small>
        </label>
      </div> -->
      <button class="btn btn-sm btn-primary m-auto" type="submit" style="width:140px">
        Sign in
      </button>
      <p>
        <small>
          <a href="#" class="text-center">Forgot password?</a>
        </small>
      </p>
      <p class="mt-5 mb-3 text-muted text-center">
        <span>
          Don't have an account?
        </span>
        <router-link to="/signup">Sign Up</router-link>
      </p>
      <p class="mt-5 mb-3 text-muted text-center">&copy; 2022</p>
    </form>
  </div>
</template>

<script>
export default {};
</script>

<style>
.form-signin{
  box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.402);
  background-color: antiquewhite !important;
}
</style>