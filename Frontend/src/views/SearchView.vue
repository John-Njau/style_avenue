<template>
  <main class="page--search">
    <div class="columns is-multiline">
      <div class="column is-12">
        <div class="search--results">
          <div class="search--results__header">
            <h1 class="title is-3">Search Results</h1>
            <p class="subtitle is-5">
              Showing {{ results.length }} results for "{{ query }}"
            </p>
          </div>
          <div class="search--results__body">
            <div class="columns is-multiline">
              <div
                class="column is-3"
                v-for="result in results"
                :key="result.id"
              >
                <div class="card">
                  <div class="card-image">
                    <figure class="image is-4by3">
                      <img :src="result.image" alt="Placeholder image" />
                    </figure>
                  </div>
                  <div class="card-content">
                    <div class="media">
                      <div class="media-content">
                        <p class="title is-4">{{ result.name }}</p>
                        <p class="subtitle is-6">{{ result.category }}</p>
                      </div>
                    </div>
                    <div class="content">
                      {{ result.description }}
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>

<script>
import axios from "axios";
import Products from "@/components/Category/Products.vue";

export default {
  components: {
    Products,
  },
  data() {
    return {
      products: [],
      query: "",
      title: "Search | Style Avenue Studio",
    };
  },
  mounted() {
    document.title = this.title;
    let uri = window.location.search.substring(1);
    let params = new URLSearchParams(uri);

    if (params.get("query")) {
      this.query = params.get("query");
      this.searchProducts();
    }
  },
  methods: {
  searchProducts()
  {
    this.$store.dispatch()
}
  }
}
</script>

<style>
</style>