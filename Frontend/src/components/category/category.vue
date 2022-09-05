<template>
  <main>
    <!-- {{ id }} -->
    {{ category }}
    <section>
      <img class="category-image" :src="category.pic" alt="" srcset="" />
      <div>
        <h1>{{ category.name }}</h1>
        <p>{{ category.description }}</p>
      </div>
      {{products}}
    </section>
    <section>
      <h2>Products in {{category.name}}</h2>
      <div class="products">
        <template v-if="products">
        <div class="product" v-for="product in products" :key="product.id">
            <img class="product-image" :src="product.image" alt="" srcset="" />
            <div>
              <img :src="product.image" alt="image" >
              <h3>{{ product.name }}</h3>
              <p>{{ product.description }}</p>
              <p>{{product.price}}</p>
              <button class="btn btn-dark">
                Add to cart
              </button>
            </div>
        </div>
      </template>
        <template v-else>
          <p>No products</p>
        </template>
      </div>
    </section>
    <!-- {{ category.name }}
    {{ category.description }}
    {{ category.image }} -->
  </main>
</template>

<script>
export default {
  props: ["id"],

  data() {
    return {
      title: "Category | Style Avenue Studio",
    };
  },
  //   methods: {
  //     getCategories() {
  //       axios
  //         .get("http://localhost:8000/categories/")
  //         .then((response) => {
  //           this.categories = response.data;
  //         })
  //         .catch((error) => {
  //           console.log(error);
  //         });
  //     },
  //   },
  computed: {
    id() {
      return this.$route.params.id;
    },
    // categoryname() {
    //   return this.$store.category.name;
    // },
  
    category() {
      return this.$store.state.category;
    },
    products() {
      return this.$store.state.products;
    },
  },
  mounted() {
    this.$store.dispatch("getCategory", this.id);
    this.$store.dispatch("getProductsCategory", this.category.name);
    console.log(this.category.name);
    document.title = this.title.toUpperCase();
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