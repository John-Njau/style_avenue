<template>
  <main>
    <div class="column is-3">
      <div class="box">
        <figure class="image mb-4">
          <img v-bind:src="product.image" />
        </figure>

        <h3 class="is-size-4">{{ product.name }}</h3>
        <p class="is-size-6 has-text-grey">${{ product.price }}</p>

        <!-- <router-link v-bind:to="product.get_absolute_url" class="button is-dark mt-4">View details</router-link> -->
      </div>
    </div>
  </main>
</template>

<script>
export default {
  name: "Products",
  props: {
    product: {
      type: Object,
    },
  },
};
</script>

<style>
</style>