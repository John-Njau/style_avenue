<template>
  <main>
    <!-- cart -->
    <section>
      <h2>Cart</h2>
      <div class="cart">
        <template v-if="cart">
          <div class="cart-item" v-for="item in cart" :key="item.id">
            <img class="cart-image" :src="item.image" alt="" srcset="" />
            <div>
              <h3>{{ item.name }}</h3>
              <p>{{ item.description }}</p>
              <p>{{ item.price }}</p>
              <button class="btn btn-dark">
                - Remove from cart
              </button>
            </div>
          </div>
        </template>
        <template v-else>
          <p>No items in cart</p>
        </template>
      </div>
    </section>
  </main>
</template>

<script>
export default {
    name: "Cart",
    props: {
        msg: String,
    },
    data() {
        return {
        title: "Cart | Style Avenue Studio",
        };
    },
    computed: {
        cart() {
        return this.$store.state.cart;
        },
    },
    mounted() {
        document.title = this.title;
    },
    

}
</script>

<style>

</style>