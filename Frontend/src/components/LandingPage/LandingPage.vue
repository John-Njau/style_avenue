<template>
  <main class="mt-0 justify-content-center">
    <!-- Display section -->

    <section class="display container-fluid mb-2">
      <div class="d-flex no-wrap img-cont">
        <div>
          <img
            class="img-fluid display-img"
            src="../../assets/images/stylemodel1.jpg"
            alt="model image"
            srcset=""
          />
        </div>
        <div>
          <img
            class="img-fluid display-img"
            src="../../assets/images/makeupitems.jpg"
            alt="image"
          />
        </div>
      </div>
      <section class="shop-div mb-2">
        <div>
          <h2 class="text-center">
            Shop for a wide range of exotic and local beauty products
          </h2>
          <marquee class="m-1">Enjoy A 10% discount on all products</marquee>
        </div>
        <div class="shop-btn text-uppercase btn">Shop Now</div>
      </section>
    </section>
    <!-- carousel -->
    <!-- <section class="mt-2">
      <div
        id="carouselExampleControls"
        class="carousel slide"
        data-bs-ride="carousel"
      >
        <div class="carousel-inner">
          <div class="carousel-item active d-flex">
            <img
              src="../../assets/images/model1.jpg"
              class="d-block h-25 w-25"
              alt="..."
            />
          </div>
          <div class="carousel-item">
            <img
              src="../../assets/images/makeupitems.jpg"
              class="d-block w-100"
              alt="..."
            />
          </div>
          <div class="carousel-item">
            <img
              src="../../assets/images/style_avenue_logo.jpg"
              class="d-block w-100"
              alt="..."
            />
          </div>
        </div>
        <button
          class="carousel-control-prev"
          type="button"
          data-bs-target="#carouselExampleControls"
          data-bs-slide="prev"
        >
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Previous</span>
        </button>
        <button
          class="carousel-control-next"
          type="button"
          data-bs-target="#carouselExampleControls"
          data-bs-slide="next"
        >
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Next</span>
        </button>
      </div>
    </section> -->
    <section class="container">
      <h4 class="text-uppercase text-center">
        <!-- <strong>Beauty Products Categories</strong> -->
      </h4>
      <div class="to-flex">
        <div v-for="(product, index) in products.results" :key="index">
          <div class="grid">
            <div class="g-col-lg-4 g-col-md-3 card mx-2">
              <div class="card-body">
                <img :src="product.image" alt="photo" class="pic" />
                <h5 class="card-title">{{ product.name }}</h5>
                <p class="card-text">{{ product.description }}</p>
                <!-- <p>{{product.category}}</p> -->
                <div class="d-flex cart-section">
                  <router-link
                    :to="{ name: 'category', params: { id: product.category } }"
                    class="btn btn-lg btn-light btn-sm"
                    >{{ product.category }} More Products
                  </router-link>
                  <div class="add-to-cart">
                    <div class="btn btn-dark btn-sm">+ Add To Cart</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <br />
    <br />
  </main>
</template>

<script>
export default {
  name: "LandingPage",
  props: [],
  data() {
    return {
      title: "Style Avenue Studio",
    };
  },
  computed: {
    categories() {
      return this.$store.state.categories;
    },
    products() {
      return this.$store.state.products;
    },
  },
  mounted() {
    this.$store.dispatch("getCategories");
    this.$store.dispatch("getProducts");
    document.title = this.title;
  },
};
</script>
<style scoped>
* {
  box-sizing: border-box;
}

.display {
  /* display: flex; */
  /* flex-direction: row; */
  justify-content: space-between;
  align-items: center;
  width: 100%;
  height: 100%;
  margin: 0 auto;
  padding: 0;
}

.to-flex {
  /* flex: 0 0 33.333%; */
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(400px, 1fr));
  /* width: 100%; */
  margin: auto auto;
  grid-auto-rows: 1fr;
  padding: 2% 0;
  gap: 20px;
  /* align-items: center; */
  /* justify-items: center; */
}

.card {
  position: relative;
  box-shadow: 1px 1px 1px 1px rgb(190, 139, 44);
  height: 350px;
}

.img-cont {
  position: relative;
}

/* .display-img{
  position: absolute;
} */

.shop-btn {
  z-index: 100;
  left: 48%;
  top: 35vh;
  border: 1px solid rgb(190, 139, 44);
  padding: 10px 20px;
  font-size: 1.2rem;
  font-weight: 300;
  cursor: pointer;
  transition: all 0.3s ease-in-out;
  position: absolute;
  margin: auto auto;
}

.shop-btn:hover {
  background-color: rgb(190, 139, 44);
  color: #fff;
}

.pic {
  /* width: 50%; */
  /* height: auto; */
  margin: 0 auto;
  height: 201px;
  object-fit: cover;
}

.cart-section {
  justify-content: space-between;
}

@media screen and (min-width: 768px) {
  .shop-btn {
    top: 38vh;
  }
}
@media screen and (min-width: 1000px) {
  .shop-btn {
    top: 70vh;
  }
}
</style>
