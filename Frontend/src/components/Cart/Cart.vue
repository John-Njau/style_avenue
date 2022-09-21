<template>
  <main>
    <!-- cart -->
    <section>
      <h2>Cart</h2>
      <div class="cart">
        <template v-if="cartTotalLength">
          <div
              class="cart-item"
              v-for="item in cart.items"
              :key="item.product.id"
              :initialItem="item"
              v-on:removeFromCart="removeFromCart"
          >
            <img class="cart-image" :src="item.image" alt="" srcset=""/>
            <div>
              <h3>{{ item.name }}</h3>
              <p>{{ item.description }}</p>
              <p>{{ item.price }}</p>
              <button class="btn btn-dark">- Remove from cart</button>
            </div>
          </div>
        </template>
        <template v-else>
          <p>No items in cart</p>
        </template>
      </div>
      <div class="column is-12 box">
        <h2 class="subtitle">Summary</h2>

        <strong>${{ cartTotalPrice.toFixed(2) }}</strong
        >, {{ cartTotalLength }} items

        <hr/>

        <router-link to="/cart/checkout" class="button is-dark"
        >Proceed to checkout
        </router-link
        >
      </div>
    </section>
  </main>
</template>

<script>
import axios from "axios";
import CartItem from "./CartItem.vue";

export default {
  name: "Cart",
  components: {
    CartItem,
  },
  data() {
    return {
      title: "Cart | Style Avenue Studio",
      cart: {
        items: [],
      },
    };
  },
  mounted() {
    this.cart = document.title = this.title;
  },
  methods: {
    removeFromCart(item) {
      this.cart.items = this.cart.items.filter(
          (i) => i.product.id !== item.product.id
      );
    },
  },
  computed: {
    cart() {
      return this.$store.state.cart;
    },
    cartTotalLength() {
      return this.cart.items.reduce((acc, curVal) => {
        return (acc += curVal.quantity);
      }, 0);
    },
    cartTotalPrice() {
      return this.cart.items.reduce((acc, curVal) => {
        return (acc += curVal.product.price * curVal.quantity);
      }, 0);
    },
  },
};
</script>

<style>
</style>