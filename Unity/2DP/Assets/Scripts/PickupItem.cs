using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[RequireComponent(typeof(Collider2D))]
public class PickupItem : MonoBehaviour
{
    public int haveScore = 1;

    private void OnTriggerEnter2D(Collider2D collision)
    {
        if (collision.CompareTag("Player"))
        {
            GameManager.Instance.GameScore += haveScore;
            gameObject.SetActive(false);
        }
    }
}
