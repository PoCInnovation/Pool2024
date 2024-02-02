<script lang="ts" context="module">
    import type { Artist } from "./Artist.svelte";

    export type User = {
        id: string,
        email: string,
        password: string,
        artists: Artist[],
    }
</script>