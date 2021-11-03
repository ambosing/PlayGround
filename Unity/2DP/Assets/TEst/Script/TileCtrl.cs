using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TileCtrl : MonoBehaviour
{
    public bool isLocate = false;
    private Renderer renderer;
    RaycastHit hit;

    private void Start()
    {
        renderer = gameObject.GetComponent<Renderer>();
    }

    public void ChangeTileColor()
    {
        if (!isLocate)
        {
            renderer.material.color = Color.red;
        }
    }

    private void Update()
    {
        TowerArranngement();
    }

    public void TowerArranngement()
    {
        //Debug.Log(Input.mousePosition);
        Debug.DrawRay(Input.mousePosition, Vector3.forward * 400, Color.red, 400);
        Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition);
        if (Physics.Raycast(ray, out hit, Mathf.Infinity))
        {
            Debug.Log(hit.transform.name);
            // spawn
            // isLocate = true;
        }
    }
}
