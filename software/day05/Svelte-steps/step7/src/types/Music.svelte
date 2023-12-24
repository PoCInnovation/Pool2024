<script lang="ts" context="module">
    import type { Artist } from "./Artist.svelte";

    export type Music = {
        id: string,
        name: string,
        rating: number,
        url: string,
        artist: Artist,
        artistId: string,
    }
</script>