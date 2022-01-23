using System.Collections;
using UnityEngine;
using Random = UnityEngine.Random;

public class ColumnMaker : MonoBehaviour
{
    private WaitForSecondsRealtime columnInterval;

    void Start()
    {
        columnInterval = new WaitForSecondsRealtime(2.5f);
        StartCoroutine(MakeColumn());
    }

    private IEnumerator MakeColumn()
    {
        yield return columnInterval;
        while (true)
        {
            if (Time.timeScale == 0)
                yield break;
            GameObject column = PoolManager.Instance.Spawn("Column");
            float randomY = Random.Range(-6.15f, -3f);
            column.transform.parent = gameObject.transform;
            column.transform.localPosition = new Vector3
                (-gameObject.transform.localPosition.x + 5, randomY, 0);
            yield return columnInterval;
        }
    }
    
    
    
}
