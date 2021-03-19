<template>
  <footer id="footer">
      <div class="links">
          <a href="https://github.com/UCLA-IEEE/project-portal/issues" class="font-fix">Report a bug</a>
      </div>

      <div class="social-media">
          <a href="https://www.facebook.com/groups/uclaieee"><img src="../../public/facebook.png" alt="Facebook"></a>
          <a href="https://www.instagram.com/uclaieee/"><img src="../../public/instagram.png" alt="Instagram"></a>
          <a href="https://uclaieee.slack.com/"><img src="../../public/slack.png" alt="Slack"></a>
          <a href="https://discord.com/invite/yjSQjVb"><img src="../../public/discord.png" alt="Discord"></a>
      </div>
  </footer>
</template>

<script>
export default {
    name: "Footer"
}
</script>

<style>
    #footer {
        position: absolute;
        bottom: 0;
        
        display: flex;
        align-items: center;
        justify-content: center;

        height: 68px;
        width: 100%;
        padding: 10px 20px;

        background-color: var(--off-white);
    }

    #footer .links {
        display: none;
    }

    #footer .links a {
        color: var(--off-black);
        text-decoration: none;
    }

    #footer .links a:hover {
        color: var(--gold);
    }

    #footer .social-media img {
        height: 25px;
        margin: 0 20px;
    }

    @media only screen and (min-width: 480px) {
        #footer {
            justify-content: space-between;
        }

        #footer .links {
            display: block;
        }

        #footer .social-media img {
            margin: 0 10px;
        }
    }
</style>