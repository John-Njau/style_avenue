<template>
  <main>
    <!-- {{ id }} -->
    {{ category }}
    <section>
      <img class="category-image" :src="category.pic" />
      <div>
        <h1>{{ category.name }}</h1>
        <p>{{ category.description }}</p>
      </div>
      {{ products }}
    </section>
    <section>
      <h2>Products in {{ category.name }}</h2>
      <div class="products">
        <template v-if="products">
          <div class="product" v-for="product in products" :key="product.id">
            <img class="product-image" :src="product.image" />
            <div>
              <img :src="product.image" alt="image" />
              <h3>{{ product.name }}</h3>
              <p>{{ product.description }}</p>
              <p>{{ product.price }}</p>
              <div class="d-flex">
                <div class="">
                  <button class="btn btn-sm btn-dark m-2">-</button>
                </div>
                <div>
                  <input type="number" class="m-2" min="1"  v-model="quantity" />
                </div>
                <div class="">
                  <p class="btn btn-sm btn-dark m-2">+</p>
                </div>
              </div>
              <div class="text-center">
                <p class="btn btn-sm btn-dark mt-2" @click="addToCart()">
                  Add To Cart
                </p>
              </div>
            </div>
          </div>
        </template>
        <template v-else>
          <p>No products</p>
        </template>
      </div>
    </section>
  </main>
</template>

<script>
import {toast} from 'bulma-toast'

export default {
  // props: ["id"],
  name: "Category",

  data() {
    return {
      title: "Category | Style Avenue Studio",
      product: {},
      quantity: 1,
    };
  },
  computed: {
    id() {
      return this.$route.params.id;
    },
    category() {
      return this.$store.state.category;
    },
    categoryname() {
      return this.$store.state.category.name;
    },
    products() {
      return this.$store.state.products;
    },
  },
  mounted() {
    this.$store.dispatch("getCategory", this.id);
    this.$store.dispatch("getProductsCategory", this.categoryname);
    // this.$store.dispatch("addToCart")

    // console.log(this.category.name);
    document.title = this.title;
  },
  methods: {
    addToCart() {
      if (isNaN(this, quantity) || this.quantity < 1) {
        this.quantity = 1;
      }

      const item = {
        product: this.product,
        quantity: this.quantity,
      };

      this.$store.commit("addToCart", item);
      console.log(item);

      toast({
        message: "The product was added to the cart",
        type: "is-success",
        dismissible: true,
        pauseOnHover: true,
        duration: 2000,
        position: "bottom-right",
      });
    },
  },
};
</script>

<style>
.category-image {
  /* width: 100%; */
  height: 400px;
}
.products {
  display: flex;
  flex-flow: row wrap;
  margin: 0 5%;
}
.product {
  /* width: 30%; */
  margin: 1%;
  border: 1px solid black;
  border-radius: 5px;
  padding: 1%;
}
</style>