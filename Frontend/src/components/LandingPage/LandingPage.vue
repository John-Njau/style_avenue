<template>
  <main class="container mt-2 d-flex justify-content-center">
    <section class="to-flex">
      <div v-for="(product, index) in products.results" :key="index">
        <div class="grid">
          <div class="g-col-lg-4 g-col-md-3 card mx-2">
            <div class="card-body">
              <img :src="product.image" alt="photo" class="pic" />
              <h5 class="card-title">{{ product.name }}</h5>
              <p class="card-text">{{ product.description }}</p>
              <!-- <p>{{product.category}}</p> -->

              <router-link
                :to="{ name: 'category', params: { id: product.category } }"
                class="btn btn-lg btn-light"
                >{{ product.category }}</router-link
              >
            </div>
          </div>
        </div>
      </div>
    </section>
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

/* .container {
  display: flex;
  flex-flow: row wrap;
} */

.to-flex {
  /* flex: 0 0 33.333%; */
  display: inline-grid;
  grid-template-columns: repeat(auto-fill, minmax(400px, 1fr));
  width: 100%;
  margin: 1% auto;
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

.pic {
  /* width: 50%; */
  /* height: auto; */
  margin: 0 auto;
  height: 201px;
  object-fit: cover;
}

/* @media screen and (min-width: 1400px) {
  .container {
    width: 100%;
  }
} */
</style>
