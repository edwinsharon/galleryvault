<a href="{% url 'view_image' feed.pk %}">
          <div class="feed">
            <img
              src="{{ feed.feedimage.url }}"
              alt="image"
              class="images"
              style="height: 200px; width: 200px"
            />
          </div>
        </a>