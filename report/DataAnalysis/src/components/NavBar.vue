<template>
  <div>
    <div class="block-header visible-xs-block">
      <button class="bob navbar-toggle visible-xs" id="menu-show" type="button" data-toggle="collapse" data-target="#menu-mobile">
        <span v-for="item in iconbar" :key="item.id" v-bind="{class:item}"></span>
      </button>

      <div class="navbar-collapse collapse" id="menu-mobile">
        <ul class="nav navbar-nav main-nav">
          <li v-for="item in navlist" :key="item.id">
            <a v-bind="{ href: '#'+item}">{{item}}</a>
          </li>
        </ul>
      </div>
      <a href="."><div class="header-logo"></div></a>
    </div>
  </div>
</template>

<script>
export default {
  name: 'NavBar',
  data () {
    return {
      iconbar: ['icon-bar', 'icon-bar', 'icon-bar'],
      navlist: ['Overview', 'DeveloperProfile']
    }
  }
}

</script>

<style>

</style>
