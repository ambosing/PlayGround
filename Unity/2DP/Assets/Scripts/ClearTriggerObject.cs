using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ClearTriggerObject : MonoBehaviour
{

    private void OnTriggerEnter2D(Collider2D collision)
    {
        GameManager.Instance.Clear();
    }
}
